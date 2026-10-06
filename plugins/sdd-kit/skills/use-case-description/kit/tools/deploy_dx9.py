#!/usr/bin/env python3
"""deploy_dx9.py — one-command deploy of a Joget DX9 app archive (.jwa) to a
registered instance, encoding the DX9 deploy deltas (rules/JOGET-DEPLOY-DELTAS.md).

    deploy_dx9.py --instance jdx7 --app taxRegistration --jwa path/to/app.jwa

Sequence (each step maps to a delta):
    resolve instance (+/jw, DD-001) -> login -> import via CSRF (DD-002/003)
    -> publish the imported version (DD-004) -> grant-admin visibility (DD-006)
    -> isolated Tomcat restart to clear the definition cache (DD-005)
    -> smoke-test the userview(s) render (the gate).

Reads ~/.joget/instances.yaml (or $JOGET_INSTANCES) for URL, install path, DB and
admin credentials; secrets come from the env vars the registry names
(`<INST>_PASSWORD`, the DB `password_env`) — nothing is stored here. PostgreSQL
instances; MySQL degrades (DB-backed steps are skipped with a warning).

Exit 0 only if the smoke-test passes.

Before anything else — before the instance is read and before anything is sent anywhere — the
deploy admits the archive (METHOD-2026-09-25-12). It reads the admission record build_app.py
wrote beside it, `<app>.admission.yaml`, and refuses an archive that has none, whose checksum is
not the one recorded, whose model is not where the record says or has changed since the build, or
whose model the interaction design gate (rule L021 of tools/validate.py; SDD-11 section 8) refuses
now; and it refuses a seed spec (`--seed`) not projected from that model. The gate is the same
function `kit validate`, `kit gen` and the build run, an error in every custody mode, and no flag
of this program turns it off. `--dry-run` runs that admission and stops, touching no server.
"""
from __future__ import annotations
import argparse, html, json, os, pathlib, re, subprocess, sys, tempfile, time, urllib.parse, zipfile
try:
    import yaml
except ImportError:
    sys.exit("deploy_dx9.py needs `pyyaml` (pip install pyyaml)")
# `requests` is needed only for the HTTP deploy path + the unauthenticated smoke; the module
# must stay importable without it (the db_import/load_seed/pg core is psql-based) so unit tests
# and hermetic CI can import it. It is loaded on demand by _need_requests().
try:
    import requests
except ImportError:
    requests = None

def log(step, msg): print(f"[{step:^9}] {msg}", flush=True)
def die(msg): print(f"[  FAIL   ] {msg}", flush=True); sys.exit(2)

def _need_requests():
    if requests is None:
        die("this path needs `requests` (pip install requests) — the DB-only steps do not")

# --------------------------------------------------------------- instance config
def load_instance(name, path):
    p = pathlib.Path(os.path.expanduser(path))
    if not p.exists(): die(f"instances file not found: {p}")
    inst = (yaml.safe_load(p.read_text()).get("instances") or {}).get(name)
    if not inst: die(f"instance '{name}' not in {p}")
    url = inst["tomcat"]["url"].rstrip("/")
    if not urllib.parse.urlparse(url).path.strip("/"):     # DD-001: ensure /jw context
        url += "/jw"; log("resolve", f"URL had no context path — using {url}")
    return inst, url

def env_secret(var):
    v = os.environ.get(var)
    if not v: die(f"env var {var} is not set (source your instance .env first)")
    return v

# ------------------------------------------------------------------- HTTP session
def csrf(session, base):                                    # DD-003 (console POSTs)
    r = session.post(base + "/csrf", headers={"FETCH-CSRF-TOKEN": "1"}, timeout=30)
    if ":" not in r.text: die("could not fetch CSRF token (FETCH-CSRF-TOKEN)")
    name, val = r.text.split(":", 1)
    return name.strip(), val.strip()

def master_token(session, base):                            # CSRFGuard token for the login form
    session.get(base + "/web/login", timeout=30)
    js = session.get(base + "/csrf", headers={"Referer": base + "/web/login"}, timeout=30).text
    m = re.search(r'masterTokenValue\s*[=:]\s*["\']([^"\']+)["\']', js)
    return m.group(1) if m else None

def login(session, base, user, pw):
    tok = master_token(session, base)
    data = {"j_username": user, "j_password": pw, "submit": "Login"}
    headers = {"Referer": base + "/web/login", "Origin": base}
    if tok:
        data["OWASP-CSRFTOKEN"] = tok
        headers["OWASP-CSRFTOKEN"] = tok
        headers["X-Requested-With"] = "XMLHttpRequest"
    r = session.post(base + "/j_spring_security_check", data=data, headers=headers, timeout=30, allow_redirects=True)
    # Joget redirects a successful login to index.jsp; a failure bounces back to /web/login.
    if "/web/login" in r.url.lower() or r.url.rstrip("/").endswith("/login"):
        die(f"login failed for {user} (bounced to {r.url})")
    log("login", f"authenticated as {user}")

def import_app(session, base, jwa):                         # DD-002/003
    n, v = csrf(session, base)
    with open(jwa, "rb") as f:
        r = session.post(base + "/web/console/app/import/submit",
                         data={n: v}, files={"appZip": (pathlib.Path(jwa).name, f, "application/zip")},
                         headers={n: v, "Referer": base + "/web/console/app/import"}, timeout=300)
    if r.status_code != 200 or "Code 404" in r.text or "Security Violation" in r.text:
        die(f"import failed (HTTP {r.status_code})")
    log("import", f"posted {pathlib.Path(jwa).name}")

def publish(session, base, app, version):                   # DD-004
    n, v = csrf(session, base)
    r = session.post(f"{base}/web/console/app/{app}/{version}/publish",
                     data={n: v}, headers={n: v}, timeout=60)
    if r.status_code != 200 or '"status":true' not in r.text.replace(" ", ""):
        die(f"publish v{version} failed (HTTP {r.status_code}: {r.text[:80]})")
    log("publish", f"published {app} v{version}")

# ------------------------------------------------------------------- DB (postgres)
# Every psql run of the kit takes the connection string WITHOUT the password (_pg_url) and the
# password through the environment psql reads (_pg_env): a password in psql's arguments stands
# in the process list for as long as psql runs (METHOD-2026-09-24-03, for this program;
# METHOD-2026-09-25-01, item 3, for run_suite.py and ui_journey.py, which import these two).
# The connection string that carried the password, _pg_dsn, was retired with that item: no
# program called it any more, and none can now build one.
def _pg_url(inst):
    db = inst["database"]
    return f"postgresql://{db['user']}@{db.get('host', 'localhost')}/{db['name']}"

def _pg_env(inst):
    """This process's environment, with the database password as PGPASSWORD when the
    registry's password variable is set (unset => local trust auth, as before)."""
    env = dict(os.environ)
    pw = os.environ.get(inst["database"].get("password_env", ""), "")
    if pw:
        env["PGPASSWORD"] = pw
    return env

def pg(inst, sql, capture=True):
    r = subprocess.run(["psql", _pg_url(inst), "-tAc", sql], capture_output=True, text=True,
                       env=_pg_env(inst))
    if r.returncode: die(f"psql error: {r.stderr.strip()[:120]}")
    return r.stdout.strip()

def pg_update(inst, sql):
    # The SQL goes to a private temporary file (created 0600 by mkstemp) that is removed after
    # use; it was /tmp/_deploy_dx9.sql, readable by every user of the machine and left behind.
    fd, path = tempfile.mkstemp(prefix="deploy_dx9_", suffix=".sql")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            fh.write(sql)
        # ON_ERROR_STOP: a bad statement (e.g. a seed row hitting a missing table) must FAIL LOUDLY,
        # never silently drop rows while psql still exits 0 (the permit_fee_config half-load, DD-009).
        r = subprocess.run(["psql", "-v", "ON_ERROR_STOP=1", _pg_url(inst), "-f", path],
                           capture_output=True, text=True, env=_pg_env(inst))
    finally:
        os.unlink(path)
    if r.returncode: die(f"psql update error: {r.stderr.strip()[:160]}")

# Joget app_fd_* system columns — the invariant every form/seed table carries.
_FD_SYS = ("id text primary key", "datecreated timestamp", "datemodified timestamp",
           "createdby text", "createdbyname text", "modifiedby text", "modifiedbyname text")

def _fd_ddl(table, colnames):
    """DDL to ensure an app_fd_* table exists with the system columns + the given c_* columns.
    Idempotent (IF NOT EXISTS). Shared by db_import (form tables) and load_seed (seed tables)."""
    out = [f"CREATE TABLE IF NOT EXISTS {table} ({', '.join(_FD_SYS)});"]
    for c in sorted(colnames):
        out.append(f"ALTER TABLE {table} ADD COLUMN IF NOT EXISTS {c} text;")
    return out

def load_seed(inst, seed_dir, fixtures=False):              # project_seed L2 -> idempotent load
    """Load projected L2 seed specs into the instance, in `order`. Idempotent: each spec's rows
    are re-inserted after deleting the rows whose deterministic id (and key column, where the
    entity has one) matches — never touching other data. The projector fixed the row ids; the
    loader adds the system columns.

    DS-* is MASTER DATA and ships with the app. DF-* is DEPLOYMENT SCENERY — the rows ui-probe
    needs before it can prove that a list opens a record — and is loaded only when `fixtures`
    is asked for. Refusing it by default is the point: a fixture taxpayer in a production
    register is a defect, and `--seed <dir>` pointed at a directory holding both must not
    quietly put one there."""
    specs = []
    for fn in sorted(os.listdir(seed_dir)):
        if not fn.endswith(".spec.yml"):
            continue
        if fn.startswith("DS-") or (fixtures and fn.startswith("DF-")):
            specs.append(yaml.safe_load(open(os.path.join(seed_dir, fn)))["seed"])
    specs.sort(key=lambda s: s.get("order", 100))
    ts = time.strftime("%Y-%m-%d %H:%M:%S")
    admin = inst["credentials"]["username"]
    sysc = ["id", "datecreated", "datemodified", "createdby", "createdbyname",
            "modifiedby", "modifiedbyname"]

    def q(v):
        # KR-16. A YAML `true` arrives here as a Python bool, and `str(True)` is `'True'`.
        # Every generated reader compares `'true'` — the dashboard SQL, a datalist's
        # extraCondition — and PostgreSQL is case-sensitive, so the row lands and no reader
        # can see it. It is normalised HERE, at the write, because this is the last point at
        # which the boolean is still a boolean: one line further on it is text and the
        # information needed to normalise it is gone.
        if isinstance(v, bool):
            v = "true" if v else "false"
        return "'" + str(v).replace("'", "''") + "'"

    stmts, total = [], 0
    for s in specs:
        table, kc, rows = s["table"], s.get("key_column"), s["rows"]
        cols_seen = {c for r in rows for c in r["columns"].keys()}
        stmts += _fd_ddl(table, cols_seen)                             # DD-009: form-less master data
        ids = ", ".join(q(r["id"]) for r in rows if r.get("id"))
        if ids:
            stmts.append(f"DELETE FROM {table} WHERE id IN ({ids});")   # idempotent by deterministic id
        if kc:
            keys = ", ".join(q(r["columns"][kc]) for r in rows if kc in r["columns"])
            if keys:
                stmts.append(f"DELETE FROM {table} WHERE {kc} IN ({keys});")
        for r in rows:
            cols = sysc + list(r["columns"].keys())
            vals = [q(r["id"]), q(ts), q(ts), q(admin), q(admin), q(admin), q(admin)] + \
                   [q(v) for v in r["columns"].values()]
            stmts.append(f"INSERT INTO {table} ({', '.join(cols)}) VALUES ({', '.join(vals)});")
            total += 1
    stmts += view_statements(seed_dir)
    if stmts:
        pg_update(inst, "\n".join(stmts))
    fx = sum(1 for s in specs if s.get("fixture"))
    log("seed", f"loaded {total} row(s) from {len(specs)} seed spec(s)"
                + (f" — {fx} of them SCENERY (DF-*), not part of the app" if fx else ""))


def view_statements(seed_dir):
    """METHOD-2026-09-28-07 (the kit's gap G5): the model's queries that are views of the database
    (project_seed DV-* specs), made after the starting rows: each table the view reads is made
    sure of first, with its entity's columns (_fd_ddl, idempotent), and the view is then made, or
    made again, from the model's statement. A view's name and statement are the model's; a
    statement the database refuses stops the load (ON_ERROR_STOP), never skipped."""
    out = []
    for fn in sorted(os.listdir(seed_dir)):
        if not (fn.startswith("DV-") and fn.endswith(".spec.yml")):
            continue
        v = yaml.safe_load(open(os.path.join(seed_dir, fn)))["view"]
        for table, cols in sorted((v.get("tables") or {}).items()):
            out += _fd_ddl(table, cols)
        out.append(f"CREATE OR REPLACE VIEW {v['name']} AS {v['sql']};")
    return out

def latest_version(inst, app):
    return pg(inst, f"select max(appversion) from app_app where appid='{app}'") or "1"

def _permission_text(p):
    """A userview permission as the grant step logs it: its class and its properties."""
    if not isinstance(p, dict):
        return repr(p)
    return f"{p.get('className') or '(none)'} {json.dumps(p.get('properties') or {}, sort_keys=True)}"

def grant_admin_visibility(inst, app, version):             # DD-006
    ids = [x for x in pg(inst, f"select id from app_userview where appid='{app}' and appversion='{version}'").splitlines() if x]
    n = 0
    for uid in ids:
        j = pg(inst, f"select json from app_userview where appid='{app}' and appversion='{version}' and id='{uid}'")
        try: d = json.loads(j)
        except Exception: continue
        blank = {"className": "", "properties": {}}
        touched = False
        # Each permission is logged by userview, category and menu before it is cleared, so
        # what the deploy took away can be read back and restored (METHOD-2026-09-24-03).
        for c in d.get("categories", []):
            cp = c.get("properties", {})
            cat = cp.get("label") or cp.get("id") or "?"
            if "permission" in cp:
                log("grant", f"userview {uid} · category {cat!r} · clearing permission "
                             f"{_permission_text(cp['permission'])}")
                cp["permission"] = blank; touched = True
            for m in c.get("menus", []):
                mp = m.get("properties", {})
                if "permission" in mp:
                    menu = mp.get("label") or mp.get("customId") or mp.get("id") or "?"
                    log("grant", f"userview {uid} · category {cat!r} · menu {menu!r} · clearing "
                                 f"permission {_permission_text(mp['permission'])}")
                    mp["permission"] = blank; touched = True
        if touched:
            body = json.dumps(d).replace("$J$", "$JJ$")
            pg_update(inst, f"UPDATE app_userview SET json=$J${body}$J$ WHERE appid='{app}' AND appversion='{version}' AND id='{uid}';")
            n += 1
    log("grant", f"cleared category permissions on {n} userview(s) (admin-visible)")
    return ids

# ----------------------------------------------------------------------- restart
def _tomcat(ip, verb):
    """Run the instance's tomcat.sh from an EMPTY environment, in a session of its own.

    The deploy's environment holds the administrator's and the database's passwords (read from
    the instance's .env), and a server started from it keeps them for as long as it runs, where
    every process that may read its environment can. Started in the caller's session and
    process group, the server also stops when the caller's group is stopped — as jdx10 did at
    04:32:15 UTC on 25 September, started from a shell of the desktop app's Desktop Commander.
    So the script gets no variable of the deploy's (tomcat.sh sets JAVA_HOME and JAVA_OPTS
    itself; the shell supplies its own search path) and starts in a new session (setsid), with
    no terminal input: as the first slice's work/s4_restart.sh did, run under `env -i` and
    POSIX::setsid (METHOD-2026-09-25-01, item 16)."""
    return subprocess.run(["./tomcat.sh", verb], cwd=ip, env={}, start_new_session=True,
                          stdin=subprocess.DEVNULL, capture_output=True, text=True)

def restart(inst, base):                                    # DD-005
    ip = inst.get("installation_path")
    if not ip or not pathlib.Path(ip, "tomcat.sh").exists():
        log("restart", "no tomcat.sh — SKIPPED (cache not cleared; restart manually)"); return
    port = inst["tomcat"]["http_port"]
    _tomcat(ip, "stop")
    for _ in range(8):
        time.sleep(2)
        if subprocess.run(["lsof", "-nP", f"-iTCP:{port}", "-sTCP:LISTEN"], capture_output=True).returncode != 0:
            break
    else:
        subprocess.run(["pkill", "-TERM", "-f", f"{ip}/apache-tomcat"], capture_output=True); time.sleep(6)
    _tomcat(ip, "start")
    for i in range(40):
        time.sleep(3)
        try:
            code = requests.get(base + "/web/json/workflow/currentUsername", timeout=5).status_code
            if code in (200, 400): log("restart", f"instance back up (~{i*3}s)"); return
        except requests.RequestException:
            pass
    die("instance did not come back up after restart")

# -------------------------------------------------------------------- smoke-test
def smoke(session, base, app, uv_ids):                      # the gate
    ok = True
    for uid in uv_ids or []:
        t = session.get(f"{base}/web/userview/{app}/{uid}", timeout=40).text
        rendered = "Code 404" not in t
        menus = len(re.findall(r'userview_menu|menu-link|pageTitle', t)) > 0
        log("smoke", f"userview {uid}: {'renders' if rendered else 'NOT FOUND'}{' · menus present' if menus else ''}")
        ok = ok and rendered
    return ok

# ---------------------------------------------------------------- dependency gate (G4)
# org.joget.* ships with Joget, enterprise included — except the families below, which are
# Joget's own marketplace plugins, installed on a server one by one. Every archive the kit builds
# binds org.joget.api.lib.AppFormAPI for its data interface API-<appId>-data (build_app.py), and
# a server without the API Builder answers every call there with 500; the gate skipped it as
# shipping with Joget (one application's deploy; METHOD-2026-09-24-03).
NOT_SHIPPED_WITH_JOGET = {
    "org.joget.api.": "Joget's API Builder, the marketplace plugin apibuilder_plugins, "
                      "installed through the console's plugin upload",
}

def _not_shipped(c):
    return next((what for prefix, what in NOT_SHIPPED_WITH_JOGET.items() if c.startswith(prefix)), None)

def _ships_with_joget(c):
    return c.startswith("org.joget.") and _not_shipped(c) is None

def required_external_classes(jwa_path):
    """The classNames the app binds that do not ship with Joget — the catalog/bespoke plugins,
    and Joget's own marketplace plugins (NOT_SHIPPED_WITH_JOGET), that MUST be installed on the
    target. Every other org.joget.* class, enterprise included, ships with Joget."""
    with zipfile.ZipFile(jwa_path) as z:
        xml = html.unescape(z.read("appDefinition.xml").decode("utf-8", "replace"))
    classes = set(re.findall(r'"className"\s*:\s*"([^"]+)"', xml))
    # Not every `className` slot holds a class. MultiPagedForm keeps its PAGE COUNT
    # in one — `"numberOfPage": {"className": "8", ...}` — so a bare regex reported
    # "8" as a missing plugin and refused an app whose plugins were all installed
    # (measured on the reference-portal wizards, jdx7, 2026-08-09). A Java class name
    # is package-qualified; a page count is not.
    return sorted(c for c in classes
                  if c and "." in c and not _ships_with_joget(c))

def installed_class_entries(inst):
    ip = inst.get("installation_path")
    pdir = pathlib.Path(ip, "wflow", "app_plugins") if ip else None
    if not pdir or not pdir.is_dir():
        return None                                          # cannot verify (remote / unknown path)
    entries = set()
    for jar in pdir.glob("*.jar"):
        try:
            with zipfile.ZipFile(jar) as z:
                entries.update(z.namelist())
        except Exception:
            pass
    return entries

def dependency_gate(inst, jwa_path):                         # G4 — refuse before import
    req = required_external_classes(jwa_path)
    if not req:
        log("deps", "no external plugin classes bound"); return
    entries = installed_class_entries(inst)
    if entries is None:
        log("deps", f"cannot verify {len(req)} plugin class(es) (no local app_plugins) — proceeding"); return
    missing = [c for c in req if (c.replace(".", "/") + ".class") not in entries]
    if missing:
        die("required plugin class(es) NOT installed on the target — install the JAR(s) into "
            "wflow/app_plugins and restart, then redeploy:\n    "
            + "\n    ".join(c + (f"  ({_not_shipped(c)})" if _not_shipped(c) else "") for c in missing))
    log("deps", f"{len(req)} external plugin class(es) verified installed")



def db_import(inst, app, jwa):                              # DD-009: credential-free definition import
    """Import a .jwa at the DEFINITION level over the registry DB creds (no HTTP admin login):
    parse appDefinition.xml -> app_app (UPSERT) + app_form/app_datalist/app_userview/app_builder
    rows (delete+insert) and CREATE the app_fd_<table> tables from the form fields. Idempotent.
    Used when the console login/import is unavailable; pairs with grant_admin_visibility + restart."""
    import xml.etree.ElementTree as ET
    zf = zipfile.ZipFile(jwa)
    root = ET.fromstring(zf.read("appDefinition.xml").decode())
    nm = root.find("name")
    app_name = nm.text if nm is not None and nm.text else app

    if "package.xpdl" in zf.namelist():                     # DD-010: xpdl not deployable at DB level
        log("db-import", "NOTE: this .jwa carries an xpdl WORKFLOW PACKAGE which --db-import CANNOT "
            "activate — Joget's workflow engine registers packages only via the console import + "
            "restart (D-003/D-026). Forms, lists, userview and the lifecycle runtime DO deploy; the "
            "xpdl process orchestration will NOT run on this path. Use the HTTP import for the "
            "process, or realize the flow via the lifecycle/approval-service instead of xpdl.")

    def recs(tag):
        return [{c.tag: (c.text or "") for c in el} for el in root.iter(tag)]

    forms, dls = recs("formDefinition"), recs("datalistDefinition")
    uvs, blds = recs("userviewDefinition"), recs("builderDefinition")

    def q(v):
        return "'" + str(v).replace("'", "''") + "'"

    tables = {}
    for f in forms:
        ids = set(re.findall(r'"id"\s*:\s*"([A-Za-z0-9_]+)"', f["json"]))
        tables.setdefault(f["tableName"], set()).update(ids)

    # app_app is UPSERTed, never deleted: nine child tables (app_env_variable, app_message, …) FK to
    # it, so DELETE would violate them. Only the definition rows we (re)generate are delete+insert.
    o = [f"DELETE FROM {t} WHERE appid={q(app)} AND appversion=1;" for t in
         ("app_form", "app_datalist", "app_userview", "app_builder")]
    o.append("INSERT INTO app_app (appid,appversion,name,published,datecreated,datemodified,meta,license,createdby) "
             f"VALUES ({q(app)},1,{q(app_name)},true,now(),now(),'','','admin') "
             "ON CONFLICT (appid,appversion) DO UPDATE SET "
             "name=EXCLUDED.name, published=true, datemodified=now();")
    for f in forms:
        o.append("INSERT INTO app_form (appid,appversion,formid,name,tablename,json,datecreated,datemodified) "
                 f"VALUES ({q(app)},1,{q(f['id'])},{q(f['name'])},{q(f['tableName'])},{q(f['json'])},now(),now());")
    for d in dls:
        o.append("INSERT INTO app_datalist (appid,appversion,id,name,description,json,datecreated,datemodified) "
                 f"VALUES ({q(app)},1,{q(d['id'])},{q(d['name'])},'',{q(d['json'])},now(),now());")
    for u in uvs:
        o.append("INSERT INTO app_userview (appid,appversion,id,name,description,json,datecreated,datemodified) "
                 f"VALUES ({q(app)},1,{q(u['id'])},{q(u['name'])},'',{q(u['json'])},now(),now());")
    for b in blds:
        o.append("INSERT INTO app_builder (appid,appversion,id,name,type,json,datecreated,datemodified) "
                 f"VALUES ({q(app)},1,{q(b['id'])},{q(b['name'])},{q(b['type'])},{q(b['json'])},now(),now());")
    for tn, cols in tables.items():
        o += _fd_ddl(f"app_fd_{tn}", (f"c_{c}" for c in cols))
    pg_update(inst, "\n".join(o))
    log("db-import", f"{len(forms)} forms, {len(dls)} datalists, {len(uvs)} userviews, "
                     f"{len(blds)} builders; {len(tables)} app_fd table(s)")
    return "1"


# ------------------------------------------------------------- admission (L021, first of all)
ADMISSION_SUFFIX = ".admission.yaml"     # build_app.py writes <app>.admission.yaml beside <app>.jwa


def _sha256(path):
    import hashlib
    return hashlib.sha256(pathlib.Path(path).read_bytes()).hexdigest()


def admit(jwa, app, seed_dir=None):
    """Refuse (exit 2) unless the archive was built by build_app.py from a model the interaction
    design gate admits now. Returns the admission record. Reads only local files."""
    jwa = pathlib.Path(jwa)
    rec_path = jwa.with_name(jwa.stem + ADMISSION_SUFFIX)
    if not rec_path.is_file():
        die(f"no admission record beside the archive ({rec_path.name} is not in {jwa.parent}): the "
            f"archive was not built by build_app.py from a model the interaction design gate "
            f"admitted, and nothing is deployed from it (METHOD-2026-09-25-12; SDD-11 section 8)")
    try:
        rec = (yaml.safe_load(rec_path.read_text(encoding="utf-8")) or {}).get("admission") or {}
    except Exception as exc:                                    # noqa: BLE001
        die(f"the admission record {rec_path} cannot be read: {exc}")
    if rec.get("app") and rec.get("app") != app:
        die(f"the admission record admits the archive as the application {rec.get('app')!r}, and "
            f"this deploy names {app!r} — refusing")
    if rec.get("jwa_sha256") != _sha256(jwa):
        die(f"the archive {jwa.name} is not the one its admission record admitted (its checksum "
            f"differs from {rec.get('jwa_sha256')}) — refusing; build it again")
    model = pathlib.Path(str(rec.get("model") or ""))
    if not model.is_file():
        die(f"the admission record names the model {model}, which is not there — refusing")
    if _sha256(model) != rec.get("model_sha256"):
        die(f"the model {model.name} has changed since the archive was built from it (its checksum "
            f"is no longer {rec.get('model_sha256')}) — refusing; generate and build again")
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
    import validate
    if validate.admit_or_refuse(model, "deploy") != 0:
        sys.exit(2)
    if seed_dir:
        sd = pathlib.Path(seed_dir)
        bad = []
        for fn in sorted(os.listdir(sd)) if sd.is_dir() else []:
            if not fn.endswith(".spec.yml"):
                continue
            sha = None
            with open(sd / fn, encoding="utf-8") as fh:
                for line in fh:
                    if line.startswith("# source_sha256:"):
                        sha = line.split(":", 1)[1].strip()
                        break
            if sha != rec.get("model_sha256"):
                bad.append(fn)
        if bad:
            die(f"{len(bad)} seed spec(s) in {sd} were not projected from the admitted model "
                f"{model.name}: {', '.join(bad[:8])}{' …' if len(bad) > 8 else ''} — refusing")
    log("admit", f"{jwa.name} admitted: built {rec.get('admitted_at')} from {model.name}, whose "
                 f"interaction design the gate admits")
    return rec


# --------------------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--instance", required=True)
    ap.add_argument("--app", required=True)
    ap.add_argument("--jwa", required=True)
    ap.add_argument("--instances", default=os.environ.get("JOGET_INSTANCES", "~/.joget/instances.yaml"))
    ap.add_argument("--no-grant-admin", action="store_true", help="keep category role-permissions (DD-006)")
    ap.add_argument("--no-restart", action="store_true", help="skip the cache-clearing restart (DD-005)")
    ap.add_argument("--no-dep-check", action="store_true", help="skip the plugin dependency gate (G4)")
    ap.add_argument("--seed", help="dir of projected L2 seed specs (project_seed) to load post-restart")
    ap.add_argument("--fixtures", action="store_true",
                    help="also load the DF-* scenery in --seed (the rows ui-probe needs). Test "
                         "instances only — never a production deploy.")
    ap.add_argument("--db-import", action="store_true", help="import at the DB definition level (no HTTP admin login; DD-009)")
    ap.add_argument("--dry-run", action="store_true",
                    help="admit the archive (the admission record, the model's checksum and the "
                         "interaction design gate, METHOD-2026-09-25-12) and stop: no instance is "
                         "read and no server is touched")
    a = ap.parse_args()
    if not pathlib.Path(a.jwa).exists(): die(f"jwa not found: {a.jwa}")
    admit(a.jwa, a.app, a.seed)                              # L021 first: before anything else
    if a.dry_run:
        log("dry-run", f"admitted; stopping before the instance '{a.instance}' is read — nothing "
                       f"was sent anywhere")
        sys.exit(0)
    _need_requests()                                        # every live path restarts + smokes over HTTP

    inst, base = load_instance(a.instance, a.instances)
    is_pg = (inst.get("database", {}).get("type") == "postgresql")

    if not a.no_dep_check:
        dependency_gate(inst, a.jwa)                         # G4: refuse missing plugins pre-import

    if getattr(a, "db_import", False):                       # DD-009: credential-free DB import
        if not is_pg:
            die("--db-import requires a postgresql instance (registry DB creds)")
        version = db_import(inst, a.app, a.jwa)
        uv_ids = grant_admin_visibility(inst, a.app, version) if not a.no_grant_admin else []
        if not a.no_restart:
            restart(inst, base)
        if a.seed:
            load_seed(inst, a.seed, a.fixtures)
        if not uv_ids:
            uv_ids = [x for x in pg(inst, f"select id from app_userview where appid='{a.app}' and appversion='{version}'").splitlines() if x]
        ok = bool(uv_ids)
        for uid in uv_ids:                                  # unauthenticated route check (no login secret)
            code = requests.get(f"{base}/web/userview/{a.app}/{uid}", timeout=40).status_code
            log("smoke", f"userview {uid}: http {code}")
            ok = ok and code in (200, 302)
        if ok:
            log("DONE", f"{a.app} v{version} DB-imported and serving on {base}/web/userview/{a.app}/{uv_ids[0]}")
            sys.exit(0)
        die("db-import smoke failed — a userview did not resolve")

    user = inst["credentials"]["username"]; pw = env_secret(inst["credentials"]["password_env"])
    s = requests.Session()
    login(s, base, user, pw)
    import_app(s, base, a.jwa)

    version = latest_version(inst, a.app) if is_pg else "1"
    if not is_pg: log("resolve", "non-postgres: DB steps skipped; assuming version 1")
    publish(s, base, a.app, version)

    uv_ids = []
    if is_pg and not a.no_grant_admin:
        uv_ids = grant_admin_visibility(inst, a.app, version)
    if not a.no_restart:
        restart(inst, base)
    # re-establish session (cookies survive; re-login to be safe after restart)
    s = requests.Session(); login(s, base, user, pw)
    if a.seed:
        if is_pg:
            load_seed(inst, a.seed, a.fixtures)              # master data (+ scenery if asked)
        else:
            log("seed", "non-postgres: seed load skipped")
    if is_pg and not uv_ids:
        uv_ids = [x for x in pg(inst, f"select id from app_userview where appid='{a.app}' and appversion='{version}'").splitlines() if x]

    if smoke(s, base, a.app, uv_ids):
        log("DONE", f"{a.app} v{version} deployed and serving on {base}/web/userview/{a.app}/{uv_ids[0] if uv_ids else '<uv>'}")
        sys.exit(0)
    die("smoke-test failed — app imported but a userview does not render")

if __name__ == "__main__":
    main()
