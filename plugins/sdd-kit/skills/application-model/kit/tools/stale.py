#!/usr/bin/env python3
"""stale — what a change to one artifact makes stale in its specification tree.

    kit stale <n> <artifact> [--tree D] [--slots F]

WHAT IT READS. The register's row <n> and its `seams.gives` cells, which name the rows that are
made from this one (01_PROCEDURE.md section 4, "after an artefact of kind N has changed"; plan
M4). The tree is the specification tree `kit spec new` scaffolds, one folder `<n>_<dir>` for
each row; the tree's root is the folder above the one the artifact stands in, or `--tree`.

Each artifact records, in the YAML block at its head (in a YAML file, at its top level), its own
version and what it was made from, each with the version it was made from:

    ---
    version: "1.1"
    made_from:
      - {path: 06_use_cases/UC-1.md, version: "1.0"}
    ---

A path is written from the tree's root. No standard fixes where an artifact records what it was
made from; this is the form the program reads, and the report of the round that wrote it names
the gap.

WHAT IT LISTS. In the folder of every row that row <n> gives to, every artifact made from the
changed one whose recorded version is not the changed artifact's version now: **stale**. Then,
from each stale artifact, every artifact made from it in the rows its own row gives to: stale by
descent, since a document made from one no longer current is itself no longer current. The
changed artifact's own claim of conformance, `_conformance/<its file name>_conformance.md`, when
its head names a checksum other than the artifact's now: stale. And every artifact in a folder
it read that records nothing it was made from: **not known**, since silence is not a third
answer (SDD-01, section 13, "A standard changes"). A folder's README.md, which the scaffold
writes, and anything under a folder whose name begins with `_` or `.` are not artifacts of the
row and are not read.

It lists and changes nothing. Exit: 0 nothing stale and nothing not known · 1 something listed
· 2 could not run.
"""
from __future__ import annotations

import argparse
import datetime
import hashlib
import os
import pathlib
import sys

import yaml

HERE = pathlib.Path(__file__).resolve().parent
KIT_ROOT = HERE.parent
SLOTS = KIT_ROOT / "templates" / "spec" / "slots.yaml"
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import conform                                                    # noqa: E402  read_head

ARTIFACT_SUFFIXES = (".md", ".yaml", ".yml")


class CouldNotRun(Exception):
    pass


def now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha256_of(path: pathlib.Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def norm(p: str) -> str:
    return os.path.normpath(str(p).strip().replace("\\", "/")).replace("\\", "/")


def record_of(path: pathlib.Path):
    """(version or None, made_from as a list of (path, version), whether it records made_from)."""
    text = path.read_text(encoding="utf-8", errors="replace")
    data = None
    if path.suffix.lower() == ".md":
        data, _, _ = conform.read_head(text)
    else:
        try:
            data = next(iter(yaml.load_all(text, Loader=yaml.BaseLoader)), None)
        except yaml.YAMLError:
            data = None
    if not isinstance(data, dict):
        return None, [], False
    version = str(data["version"]).strip() if data.get("version") not in (None, "") else None
    raw = data.get("made_from")
    if raw is None:
        return version, [], False
    entries = raw if isinstance(raw, list) else [raw]
    out = []
    for e in entries:
        if isinstance(e, dict) and e.get("path"):
            out.append((norm(e["path"]), str(e.get("version", "")).strip()))
    return version, out, bool(out)


def artifacts_in(folder: pathlib.Path) -> list[pathlib.Path]:
    if not folder.is_dir():
        return []
    out = []
    for f in sorted(folder.rglob("*")):
        rel = f.relative_to(folder)
        if not f.is_file() or f.suffix.lower() not in ARTIFACT_SUFFIXES:
            continue
        if f.name == "README.md" or any(p.startswith(("_", ".")) for p in rel.parts):
            continue
        out.append(f)
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="kit stale", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("n", help="the row of the register the changed artifact belongs to")
    ap.add_argument("artifact", type=pathlib.Path)
    ap.add_argument("--tree", type=pathlib.Path,
                    help="the specification tree's root (default: above the artifact's slot)")
    ap.add_argument("--slots", type=pathlib.Path, default=SLOTS)
    a = ap.parse_args(argv)
    try:
        return _run(a)
    except CouldNotRun as exc:
        print(f"kit stale: could not run: {exc}", file=sys.stderr)
        return 2


def _run(a) -> int:
    try:
        spec = yaml.safe_load(a.slots.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as exc:
        raise CouldNotRun(f"the register {a.slots} cannot be read: {exc}")
    rows = {str(s.get("n")): s for s in (spec or {}).get("slots") or []}
    n = a.n if a.n in rows else (a.n.zfill(2) if a.n.isdigit() else a.n)
    if n not in rows:
        raise CouldNotRun(f"the register has no row {a.n!r}; its rows are {', '.join(rows)}")
    folder = {k: f"{k}_{r.get('dir')}" for k, r in rows.items()}
    artifact = a.artifact.resolve()
    if not artifact.is_file():
        raise CouldNotRun(f"the artifact {a.artifact} is not there")

    if a.tree:
        tree = a.tree.resolve()
    else:
        tree = next((p.parent for p in artifact.parents if p.name == folder[n]), None)
        if tree is None:
            raise CouldNotRun(f"{a.artifact} does not stand in a folder {folder[n]}, the folder "
                              f"of row {n}; name the tree with --tree")
    try:
        changed_rel = artifact.relative_to(tree).as_posix()
    except ValueError:
        raise CouldNotRun(f"{a.artifact} is not inside the tree {tree}")
    version, _, _ = record_of(artifact)
    if not version:
        raise CouldNotRun(f"{changed_rel} records no version of its own at its head, so "
                          "nothing can be compared with it")
    sha = sha256_of(artifact)

    def gives(k: str) -> list[str]:
        return [str(g.get("to")) for g in ((rows[k].get("seams") or {}).get("gives") or [])
                if str(g.get("to")) in rows]

    stale: list[tuple[str, str]] = []            # (path, why)
    silent: dict[str, None] = {}
    read_folders: set[str] = set()
    records: dict[str, tuple] = {}

    def made_from_here(target_rows, source_rel):
        for k in target_rows:
            for f in artifacts_in(tree / folder[k]):
                rel = f.relative_to(tree).as_posix()
                if rel not in records:
                    records[rel] = (k,) + record_of(f)
                read_folders.add(folder[k])
                _, _, made, has = records[rel]
                if not has:
                    silent[rel] = None
                    continue
                for p, v in made:
                    if p == source_rel:
                        yield rel, k, v

    listed: set[str] = set()
    frontier: list[tuple[str, str]] = []
    for rel, k, v in made_from_here(gives(n), changed_rel):
        if v != version and rel not in listed:
            listed.add(rel)
            stale.append((rel, f"made from {changed_rel} version {v or '(none recorded)'}; "
                               f"its version now is {version}"))
            frontier.append((rel, k))
    while frontier:
        src, k = frontier.pop(0)
        for rel, k2, _ in made_from_here(gives(k), src):
            if rel not in listed and rel != changed_rel:
                listed.add(rel)
                stale.append((rel, f"made from {src}, which is stale"))
                frontier.append((rel, k2))

    claim = artifact.parent / "_conformance" / f"{artifact.name}_conformance.md"
    if claim.is_file():
        head, _, _ = conform.read_head(claim.read_text(encoding="utf-8"))
        written = str((head or {}).get("artifact_sha256", "")).strip()
        if written != sha:
            stale.append((claim.relative_to(tree).as_posix() if claim.is_relative_to(tree)
                          else str(claim),
                          f"the claim of conformance was written against sha256 "
                          f"{(written or '(none)')[:12]}; the artifact is now {sha[:12]}"))

    print(f"kit stale {n} {changed_rel} at {now()}")
    print(f"  register  {a.slots}")
    print(f"  tree      {tree}")
    print(f"  changed   {changed_rel}, version {version}, sha256 {sha[:12]}")
    print(f"  made from it, by the register: rows {', '.join(gives(n)) or 'none'}; "
          f"folders read: {', '.join(sorted(read_folders)) or 'none'}")
    for rel, why in stale:
        print(f"  stale      {rel} — {why}")
    for rel in silent:
        print(f"  not known  {rel} — records nothing it was made from")
    print(f"  {len(stale)} stale, {len(silent)} not known")
    return 1 if stale or silent else 0


if __name__ == "__main__":
    sys.exit(main())
