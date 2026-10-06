#!/usr/bin/env python3
"""ui_journey.py — does a person get all the way THROUGH? (ADR-093 §2)

`kit ui-probe` proves each menu keeps the promise its type makes: a form submits, a listed
record opens. That is reachability, and it is not enough. On 2026-08-02 every menu in the
registration app kept its promise while three procedures were still impassable end to end —
the applicant could create a draft and had no surface anywhere to submit it. Reachability of
each step says nothing about the path.

Journeys are declared, not scripted, so they live with the app instead of in someone's
terminal history. Steps:

    open: <menu customId>              go to a menu
    fill: {field: value}               fill named fields (select or input)
    submit:                            click the form's submit control
    open_first_row: <menu customId>    open the first data row of a list/crud menu
    expect_rows: {menu: <id>, min: 1}  a list has (or has not) data
    expect_actions: [submit, ...]      the lifecycle actions offered here, exactly
    act: <transition>                  press the move's button and save its form (item 3 of
                                       METHOD-2026-09-25-04; {move, fill} to give its reason)
    expect_error: <substring>          the page shows this validation message

CLEANUP IS PART OF THE CONTRACT. A journey writes real records through real screens, and the
acceptance suite counts records. Every row a journey creates is deleted at the end, by diffing
the app's tables around the run — this tool exists because I broke that suite twice in one
afternoon by clicking through the app it tests.

    ui_journey.py <app.yaml> --journeys design/journeys.yaml --instance jdx9

Exit: 0 every journey completed · 1 a journey did not · 3 setup error, or psql could not read
the application's tables, before the run or for the clean-up (METHOD-2026-09-25-01, item 3).
"""
from __future__ import annotations

import argparse
import datetime
import pathlib
import re
import subprocess
import sys

try:
    import yaml
except ImportError:
    sys.exit("ui_journey.py needs pyyaml")

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import deploy_dx9 as dep  # instance resolution, the database's address and psql's environment

EDITABLE = ("input:not([type=hidden]):not([type=submit]):not([type=button]):not([disabled])"
            ":not([readonly]), textarea:not([readonly]):not([disabled]), select:not([disabled])")
# Tried IN ORDER, most specific first. A single comma-joined selector was wrong: Playwright's
# `.first` is first in DOM ORDER, not first matching sub-selector, so a stray `.btn-primary`
# earlier on the page (Joget's CRUD toolbar has one) got clicked instead of the form's Submit.
# Nothing errored, nothing saved, and the journey blamed the officer queue three steps later.
SUBMIT_ORDER = ("#form-submit-button", ".form-button-submit",
                "button[type=submit]", "input[type=submit]")
SUBMIT = ", ".join(SUBMIT_ORDER)
DATA_ROWS = "e=>e.filter(r=>r.querySelectorAll('td').length>1)"


def _as_displayed(placeholder: str | None, value: str) -> str:
    """Journeys declare dates ISO. A Joget DatePicker accepts only what its own placeholder
    says, and the generated pickers carry no explicit display format, so they inherit the
    server locale — on jdx9 that is MM/DD/YYYY. Typing 2031-07-15 got "Invalid date format"
    and, because nothing else on the page said so, read downstream as a missing record.
    Translate here; the journey stays readable and locale-independent."""
    if not placeholder or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        return value
    y, m, d = value.split("-")
    out = placeholder.upper()
    if "YYYY" not in out or "MM" not in out or "DD" not in out:
        return value
    return out.replace("YYYY", y).replace("MM", m).replace("DD", d)


class Db:
    """How psql reaches the instance's database: the connection string WITHOUT the password
    (deploy_dx9._pg_url) and the password in the environment psql reads (deploy_dx9._pg_env,
    PGPASSWORD). A password in psql's arguments stands in the process list for as long as psql
    runs (METHOD-2026-09-25-01, item 3)."""

    def __init__(self, url: str, env: dict | None = None):
        self.url, self.env = url, env

    @classmethod
    def of(cls, inst: dict) -> "Db":
        return cls(dep._pg_url(inst), dep._pg_env(inst))


class DbError(RuntimeError):
    """psql could not read the application's tables — not a table that is merely absent."""


def _sql(db: Db, q: str) -> str:
    r = subprocess.run(["psql", db.url, "-tA", "-v", "ON_ERROR_STOP=1", "-c", q],
                       capture_output=True, text=True, env=db.env)
    if r.returncode != 0:
        raise RuntimeError(r.stderr.strip()[-300:])
    return r.stdout.strip()


def table_ids(db: Db, tables: list[str]) -> dict[str, set[str]]:
    """The row ids of each table that exists. A table not created yet has nothing to diff and
    is left out, which the database's own catalogue says; every other failure of psql — the
    server down, the password refused, the database misnamed — is raised as DbError. It used to
    be swallowed as though every table were absent, so a run that could not read the database
    diffed nothing and removed nothing, and said nothing (METHOD-2026-09-25-01, item 3)."""
    if not tables:
        return {}
    names = ", ".join("'" + t.lower().replace("'", "''") + "'" for t in tables)
    out = {}
    try:
        present = set(_sql(db, "select lower(table_name) from information_schema.tables "
                               f"where lower(table_name) in ({names})").split())
        for t in tables:
            if t.lower() not in present:
                continue                               # table not created yet — nothing to diff
            rows = _sql(db, f"select id from {t}")
            out[t] = {r for r in rows.splitlines() if r}
    except RuntimeError as e:
        raise DbError(f"psql could not read the application's tables: {e}") from e
    return out


class Journey:
    def __init__(self, page, base, app_id, uv_id):
        self.pg, self.base, self.app, self.uv = page, base, app_id, uv_id
        self.log: list[str] = []

    def url(self, menu):
        return f"{self.base}/web/userview/{self.app}/{self.uv}/_/{menu}"

    def _abs(self, href):
        return (self.base.rsplit("/jw", 1)[0] + href) if href.startswith("/") else href

    def _actions(self):
        # METHOD-2026-09-25-04, item 3: the moves offered here are the act bar's enabled
        # buttons (a.kit-act, each naming its move), no longer the options of an Action select
        return self.pg.eval_on_selector_all(".kit-acts a.kit-act[data-transition]",
                                            "e=>e.map(a=>a.getAttribute('data-transition'))")

    def _click_submit(self):
        for sel in SUBMIT_ORDER:
            loc = self.pg.locator(sel)
            if loc.count():
                loc.first.click()
                self.pg.wait_for_load_state("networkidle", timeout=30000)
                # Joget paints the body after networkidle: read the page too soon and it says
                # only "Please wait...", so a validation refusal scrapes as a clean submit.
                try:
                    self.pg.wait_for_selector(".form-cell, .form-container, .form-message",
                                              timeout=15000)
                except Exception:                      # noqa: BLE001  a list page has neither
                    pass
                self.pg.wait_for_timeout(600)
                return
        raise AssertionError("no submit control on this page")

    def _read_list(self, menu: str, enough=None):
        """Load a list menu and read its data rows back.

        Joget serves a STALE result set on the first load of a list after the data behind it
        changed — measured on jdx9 2026-08-03: create a draft, submit it, ask the officer queue
        and it is empty; ask again, unchanged, and the row is there. Four of five journeys were
        failing on this and every one of them looked like an application defect. So: always
        discard one load, and when the journey expects MORE rows, give the cache a bounded
        number of further chances rather than one. Never retry when it expects FEWER — a stale
        empty page must not be allowed to prove that nothing leaked into a queue.
        """
        rows = []
        for attempt in range(4 if enough else 2):
            if attempt:
                self.pg.wait_for_timeout(700)
            self.pg.goto(self.url(menu), wait_until="networkidle", timeout=30000)
            rows = self.pg.eval_on_selector_all(
                "table tbody tr",
                DATA_ROWS + ".map(r=>Array.from(r.querySelectorAll('td'))"
                            ".map(c=>(c.textContent||'').trim()).filter(Boolean).join(' | '))")
            if attempt and (enough is None or enough(rows)):
                break
        return rows

    def _refused(self, what: str):
        """A Joget form that fails validation re-renders itself with the messages inline and
        HTTP 200. Clicking submit is therefore not evidence that anything was saved — the
        first version of this runner logged `act submit` for a row that never left draft, and
        the failure surfaced three steps later as an empty queue, pointing at the wrong thing.
        Read the messages back and fail where the refusal actually happened."""
        msgs = self.pg.eval_on_selector_all(
            ".form-error-message, .form-errors, .form-error, .alert-danger",
            "e=>e.map(x=>(x.textContent||'').trim()).filter(Boolean)")
        seen, uniq = set(), []
        for m in msgs:
            if m not in seen:
                seen.add(m)
                uniq.append(m)
        if uniq:
            raise AssertionError(f"{what} was refused: {'; '.join(uniq)[:300]}")

    def step(self, s: dict, nxt: dict | None = None):
        (verb, arg), = s.items()
        pg = self.pg
        # A journey whose NEXT step is `expect_error` is asserting the refusal on purpose.
        check = not (isinstance(nxt, dict) and "expect_error" in nxt)
        if verb == "open":
            pg.goto(self.url(arg), wait_until="networkidle", timeout=30000)
            self.log.append(f"open {arg}")
        elif verb == "fill":
            for k, v in arg.items():
                sel = pg.locator(f"select[name='{k}']")
                if sel.count():
                    sel.select_option(value=str(v))
                    continue
                inp = pg.locator(f"[name='{k}']")
                if not inp.count():
                    raise AssertionError(f"field '{k}' is not on this page")
                if inp.first.get_attribute("readonly") is not None:
                    # A Joget DatePicker renders as a readonly input you populate from the
                    # calendar widget, so `readonly` alone is not "unfillable". The distinction
                    # matters: the READONLY finding is what caught is_material — a plain
                    # TextField, required and frozen, on a form nobody could submit — and a
                    # runner that cried wolf on every date field would have lost that.
                    cls = (inp.first.get_attribute("class") or "") + \
                        (inp.first.get_attribute("type") or "")
                    if "date" not in cls.lower():
                        raise AssertionError(f"field '{k}' is READONLY — nobody can fill it")
                    pg.eval_on_selector(
                        f"[name='{k}']",
                        "(el, val) => { el.value = val;"
                        " el.dispatchEvent(new Event('input', {bubbles:true}));"
                        " el.dispatchEvent(new Event('change', {bubbles:true})); }",
                        _as_displayed(inp.first.get_attribute("placeholder"), str(v)))
                    continue
                inp.first.fill(str(v))
            self.log.append(f"fill {', '.join(arg)}")
        elif verb == "submit":
            self._click_submit()
            if check:
                self._refused("submit")
            self.log.append("submit")
        elif verb == "open_first_row":
            pg.goto(self.url(arg), wait_until="networkidle", timeout=30000)
            links = pg.eval_on_selector_all("table tbody a[href*='_mode=']",
                                            "e=>e.map(x=>x.getAttribute('href'))")
            if not links:
                raise AssertionError(f"{arg}: no row to open")
            pg.goto(self._abs(links[0]), wait_until="networkidle", timeout=30000)
            self.log.append(f"open a record from {arg}")
        elif verb == "open_row_matching":
            # `open_first_row` is ambiguous the moment the instance holds anyone else's data —
            # j05 opened the acceptance suite's leftover case and reported "no actions offered",
            # which was true of that record and said nothing about the one the journey made.
            menu, needle = arg["menu"], str(arg["text"])
            self._read_list(menu, enough=lambda r: any(needle in x for x in r))
            href = pg.eval_on_selector_all(
                "table tbody tr",
                "(rows, needle) => { for (const r of rows) {"
                " if ((r.textContent||'').includes(needle)) {"
                "  const a = r.querySelector(\"a[href*='_mode=']\"); if (a) return a.getAttribute('href'); } }"
                " return null; }", needle)
            if not href:
                raise AssertionError(f"{menu}: no openable row containing {needle!r}")
            pg.goto(self._abs(href), wait_until="networkidle", timeout=30000)
            self.log.append(f"open the row matching {needle!r} in {menu}")
        elif verb == "expect_rows":
            lo, hi = arg.get("min", 0), arg.get("max")
            got = self._read_list(arg["menu"],
                                  enough=(lambda r: len(r) >= lo) if lo else None)
            n = len(got)
            if n < lo or (hi is not None and n > hi):
                # Say WHAT was there, not just how many. A bare count sent an afternoon after
                # a phantom row that turned out to be the queue's own header markup.
                raise AssertionError(f"{arg['menu']}: {n} row(s), wanted "
                                     f"min {lo}{'' if hi is None else f' max {hi}'}"
                                     + (f" — rows: {got[:3]}" if got else ""))
            self.log.append(f"{arg['menu']} has {n} row(s)")
        elif verb == "expect_actions":
            got = self._actions()
            if sorted(got) != sorted(arg):
                raise AssertionError(f"actions offered {got}, wanted {arg}")
            self.log.append(f"actions offered = {got}")
        elif verb == "act":
            wanted = arg["move"] if isinstance(arg, dict) else arg
            if wanted not in self._actions():
                raise AssertionError(f"action '{wanted}' is not offered here "
                                     f"(offered: {self._actions()})")
            # the move's button opens the move's own form with the record carried; the move is
            # made by saving that form (a `fill` step before `act` fills the record's form, so a
            # move's reason is given with `act: {move: <id>, fill: {reason: ...}}`)
            move = arg["move"] if isinstance(arg, dict) else arg
            pg.locator(f".kit-acts a.kit-act[data-transition='{move}']").first.click()
            pg.wait_for_load_state("networkidle", timeout=30000)
            for k, v in ((arg.get("fill") or {}) if isinstance(arg, dict) else {}).items():
                sel = f"[name='{k}']"
                if pg.locator(f"select{sel}").count():
                    pg.select_option(f"select{sel}", str(v))
                else:
                    pg.fill(sel, str(v))
            self._click_submit()
            if check:
                self._refused(f"act {arg}")
            self.log.append(f"act {arg}")
        elif verb == "expect_error":
            body = pg.inner_text("body")
            if arg.lower() not in body.lower():
                raise AssertionError(f"expected the page to say {arg!r}")
            self.log.append(f"refused with {arg!r}")
        else:
            raise AssertionError(f"unknown step '{verb}'")


def login(page, base, user, password):
    page.goto(f"{base}/web/login", wait_until="networkidle", timeout=30000)
    page.locator("input[type=text]:visible").first.fill(user)
    pw = page.locator("input[type=password]:visible").first
    pw.fill(password)
    pw.press("Enter")
    page.wait_for_load_state("networkidle", timeout=30000)
    if "/web/login" in page.url:
        sys.exit("ui_journey: login failed")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("app", type=pathlib.Path)
    ap.add_argument("--journeys", type=pathlib.Path)
    ap.add_argument("--instance", required=True)
    ap.add_argument("--instances")
    ap.add_argument("--headed", action="store_true")
    ap.add_argument("--keep", action="store_true",
                    help="do NOT delete what the run created (for inspecting a failure)")
    a = ap.parse_args()

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("ui_journey: playwright is not installed — `pip install playwright && "
              "playwright install chromium`. A probe that cannot run must SAY so.")
        return 3

    model = yaml.safe_load(a.app.read_text(encoding="utf-8"))
    app_id = (model.get("app") or {}).get("id")
    uv_id = (model.get("navigation") or {}).get("userview_id")
    jfile = a.journeys or (a.app.parent / "design" / "journeys.yaml")
    if not jfile.is_file():
        print(f"ui_journey: no journeys at {jfile}")
        return 3
    journeys = (yaml.safe_load(jfile.read_text(encoding="utf-8")) or {}).get("journeys") or []

    inst = dep.resolve(a.instance, a.instances) if hasattr(dep, "resolve") else None
    if inst is None:                                   # fall back to the registry shape directly
        reg = yaml.safe_load(pathlib.Path(
            pathlib.Path.home() / ".joget" / "instances.yaml").read_text(encoding="utf-8"))
        inst = (reg.get("instances") or {})[a.instance]
        inst.setdefault("_defaults", reg.get("joget_defaults") or {})
    base = ((inst.get("tomcat") or {}).get("url") or "").rstrip("/")
    admin = ((inst.get("_defaults") or {}).get("admin") or {})
    user = (inst.get("credentials") or {}).get("username") or admin.get("username", "admin")
    import os
    pwd = os.environ.get((inst.get("credentials") or {}).get("password_env") or "") \
        or admin.get("password")
    db = Db.of(inst)

    tables = sorted({e["table"] for e in model.get("entities", []) if e.get("table")})
    tables = [f"app_fd_{t}" for t in tables]
    try:
        before = table_ids(db, tables)
    except DbError as e:
        # without the tables read first, nothing the journeys create could be told apart and
        # removed afterwards: the run does not start (item 3)
        print(f"ui_journey: {e} — no journey was run")
        return 3

    results = []
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=not a.headed)
        page = browser.new_page()
        login(page, base, user, pwd)
        for j in journeys:
            runner = Journey(page, base, app_id, uv_id)
            r = {"id": j.get("id"), "name": j.get("name"), "ok": True, "failed_at": None,
                 "steps": []}
            steps = j.get("steps") or []
            for i, s in enumerate(steps):
                try:
                    runner.step(s, steps[i + 1] if i + 1 < len(steps) else None)
                except Exception as e:                 # noqa: BLE001
                    r["ok"] = False
                    r["failed_at"] = {"step": i + 1, "was": s, "why": str(e).splitlines()[0][:200]}
                    break
            r["steps"] = runner.log
            results.append(r)
        browser.close()

    # Cleanup: every row these journeys created, and nothing else.
    removed, cleanup_failed = 0, None
    if not a.keep:
        try:
            after = table_ids(db, tables)
            for t, ids in after.items():
                new = ids - before.get(t, set())
                if new:
                    lst = ",".join("'" + i.replace("'", "''") + "'" for i in new)
                    _sql(db, f"delete from {t} where id in ({lst})")
                    removed += len(new)
        except RuntimeError as e:                      # DbError included
            cleanup_failed = str(e)

    for r in results:
        print(f"  {'ok  ' if r['ok'] else 'FAIL'} {r['id']}: {r['name']}")
        for s in r["steps"]:
            print(f"        · {s}")
        if not r["ok"]:
            f = r["failed_at"]
            print(f"        ! step {f['step']} {f['was']} -> {f['why']}")
    bad = [r for r in results if not r["ok"]]
    print(f"ui-journey: {len(results) - len(bad)}/{len(results)} journeys completed"
          + (f" · {len(bad)} FAILING" if bad else "")
          + (f" · {removed} row(s) created and removed" if removed else "")
          + (" · KEPT (--keep)" if a.keep else ""))
    if cleanup_failed:
        print(f"ui_journey: the clean-up FAILED — {cleanup_failed}; the rows these journeys "
              f"created were not removed")

    res = a.app.parent / "design" / "ui-journey-result.yaml"
    res.parent.mkdir(parents=True, exist_ok=True)
    res.write_text(yaml.safe_dump({"ui_journey_result": {
        "app": app_id, "instance": a.instance,
        "ran_at": datetime.datetime.now().isoformat(timespec="seconds"),
        "total": len(results), "completed": len(results) - len(bad),
        "exit": 1 if bad else 0,
        "failing": [{"id": r["id"], "at": r["failed_at"]} for r in bad],
    }}, sort_keys=False, allow_unicode=True), encoding="utf-8")
    print(f"result -> {res}")
    return 3 if cleanup_failed else (1 if bad else 0)


if __name__ == "__main__":
    sys.exit(main())
