"""Phase 1 project — Day 2 reference implementation.

End-of-Day-2 deliverable: all four subcommands work end-to-end.
Builds on Day 1's Contact/Roster/load_csv. Adds:
  - cmd_find: O(1) by_email/by_phone, O(n) by_regex
  - cmd_dupes: defaultdict-grouped on (name_initials, phone_digits)
  - cmd_export: write a clean normalized CSV
  - @timed decorator wrapped around find + dupes
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


def timed(fn: Callable) -> Callable:
    @wraps(fn)
    def wrapper(*a, **kw):
        t0 = time.perf_counter()
        try:
            return fn(*a, **kw)
        finally:
            elapsed_ms = (time.perf_counter() - t0) * 1000
            print(f"[{fn.__name__}: {elapsed_ms:.2f} ms]", file=sys.stderr)
    return wrapper


def _normalize_phone(s: str) -> str:
    return re.sub(r"\D", "", s or "")


def _detect_delim(first_line: str) -> str:
    return ";" if first_line.count(";") > first_line.count(",") else ","


def load_csv(path: Path) -> list[dict]:
    text = path.read_text()
    if not text.strip():
        return []
    first, _, _ = text.partition("\n")
    delim = _detect_delim(first)
    contacts: list[dict] = []
    for row in csv.DictReader(text.splitlines(), delimiter=delim):
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
    if args.regex:
        hits = roster.find_regex(args.regex)
        for c in hits:
            print(f"{c['name']}  {c['email']}  {c['phone']}")
        return 0 if hits else 1
    print("find: pass one of --email --phone --regex", file=sys.stderr)
    return 2


@timed
def cmd_dupes(args: argparse.Namespace) -> int:
    roster = Roster(load_csv(Path(args.path)))
    groups: dict = defaultdict(list)
    for c in roster.contacts:
        groups[_dupe_key(c)].append(c)
    found = False
    for key, members in groups.items():
        if len(members) > 1:
            found = True
            print(f"-- group {key} --")
            for m in members:
                print(f"  {m['name']}  {m['email']}  {m['phone']}")
    return 0 if found else 1


def cmd_export(args: argparse.Namespace) -> int:
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
    p = argparse.ArgumentParser(prog="contacts")
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
