"""Phase 1 project — Day 3 reference implementation (final).

End-of-Phase-1 deliverable: tested, hardened, polished.

Day 3 changes vs. Day 2:
  - Robust loader: skips malformed rows silently; empty file => [].
  - Each subcommand has its own friendly error path (no traceback on
    file-not-found, permission-denied, missing args).
  - --help banner.
  - Dupes output sorted deterministically.
  - List prints contact count to stderr (so it stays out of pipes).
  - Exit codes follow the README: 0 success, 1 nothing-found, 2 usage.
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
import time
from collections import defaultdict
from collections.abc import Callable
from functools import wraps
from pathlib import Path


BANNER = "contacts — load, search, dedupe, export a small contacts CSV."


def timed(fn: Callable) -> Callable:
    @wraps(fn)
    def wrapper(*a, **kw):
        t0 = time.perf_counter()
        try:
            return fn(*a, **kw)
        finally:
            print(f"[{fn.__name__}: {(time.perf_counter() - t0) * 1000:.2f} ms]",
                  file=sys.stderr)
    return wrapper


def _normalize_phone(s: str) -> str:
    return re.sub(r"\D", "", s or "")


def _detect_delim(first_line: str) -> str:
    return ";" if first_line.count(";") > first_line.count(",") else ","


def load_csv(path: Path) -> list[dict]:
    """Load a contacts CSV. Empty file → []. Malformed rows skipped."""
    try:
        text = path.read_text()
    except FileNotFoundError:
        print(f"contacts: file not found: {path}", file=sys.stderr)
        raise SystemExit(2)
    except PermissionError:
        print(f"contacts: permission denied: {path}", file=sys.stderr)
        raise SystemExit(2)
    if not text.strip():
        return []
    first, _, _ = text.partition("\n")
    delim = _detect_delim(first)
    contacts: list[dict] = []
    reader = csv.DictReader(text.splitlines(), delimiter=delim)
    expected = set(reader.fieldnames or [])
    for row in reader:
        if not expected.issubset(row.keys()):
            continue  # malformed; skip
        contacts.append({
            "name": (row.get("name") or "").strip(),
            "email": (row.get("email") or "").strip().lower(),
            "phone": _normalize_phone(row.get("phone") or ""),
        })
    return contacts


class Roster:
    def __init__(self, contacts: list[dict]) -> None:
        self.contacts = contacts
        self.by_email = {c["email"]: c for c in contacts if c["email"]}
        self.by_phone = {c["phone"]: c for c in contacts if c["phone"]}

    def sorted_by_name(self) -> list[dict]:
        return sorted(self.contacts, key=lambda c: c["name"].lower())

    def find_email(self, email: str) -> dict | None:
        return self.by_email.get(email.strip().lower())

    def find_phone(self, phone: str) -> dict | None:
        return self.by_phone.get(_normalize_phone(phone))

    def find_regex(self, pattern: str) -> list[dict]:
        rx = re.compile(pattern)
        return [c for c in self.contacts if rx.search(c["name"])]


def _dupe_key(c: dict) -> tuple[str, str]:
    initials = "".join(p[:1] for p in c["name"].lower().split())
    return (initials, c["phone"])


def cmd_list(args: argparse.Namespace) -> int:
    roster = Roster(load_csv(Path(args.path)))
    for c in roster.sorted_by_name():
        print(f"{c['name']:<24}  {c['email']:<28}  {c['phone']}")
    print(f"({len(roster.contacts)} contacts)", file=sys.stderr)
    return 0


@timed
def cmd_find(args: argparse.Namespace) -> int:
    flags = [f for f in (args.email, args.phone, args.regex) if f]
    if not flags:
        print("find: pass one of --email --phone --regex", file=sys.stderr)
        return 2
    roster = Roster(load_csv(Path(args.path)))
    if args.email:
        c = roster.find_email(args.email)
        if c is None:
            return 1
        print(f"{c['name']}  {c['email']}  {c['phone']}")
        return 0
    if args.phone:
        c = roster.find_phone(args.phone)
        if c is None:
            return 1
        print(f"{c['name']}  {c['email']}  {c['phone']}")
        return 0
    hits = roster.find_regex(args.regex)
    for c in hits:
        print(f"{c['name']}  {c['email']}  {c['phone']}")
    return 0 if hits else 1


@timed
def cmd_dupes(args: argparse.Namespace) -> int:
    roster = Roster(load_csv(Path(args.path)))
    groups: dict = defaultdict(list)
    for c in roster.contacts:
        groups[_dupe_key(c)].append(c)
    found = False
    sorted_groups = sorted(
        ((k, members) for k, members in groups.items() if len(members) > 1),
        key=lambda kv: kv[1][0]["name"].lower(),
    )
    for key, members in sorted_groups:
        found = True
        print(f"-- group {key} --")
        for m in members:
            print(f"  {m['name']}  {m['email']}  {m['phone']}")
    return 0 if found else 1


def cmd_export(args: argparse.Namespace) -> int:
    if not args.out:
        print("export: missing output path", file=sys.stderr)
        return 2
    contacts = load_csv(Path(args.path))
    out = Path(args.out)
    with out.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["name", "email", "phone"])
        w.writeheader()
        for c in contacts:
            w.writerow(c)
    print(f"wrote {len(contacts)} contacts to {out}", file=sys.stderr)
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="contacts", description=BANNER)
    sub = p.add_subparsers(dest="cmd", required=True)
    for name, fn in [("list", cmd_list), ("find", cmd_find),
                     ("dupes", cmd_dupes), ("export", cmd_export)]:
        sp = sub.add_parser(name)
        sp.add_argument("path")
        if name == "find":
            sp.add_argument("--email")
            sp.add_argument("--phone")
            sp.add_argument("--regex")
        if name == "export":
            sp.add_argument("out")
        sp.set_defaults(func=fn)
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
