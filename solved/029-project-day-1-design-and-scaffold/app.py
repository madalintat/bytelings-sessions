"""Phase 1 project — Day 1 reference implementation.

End-of-Day-1 deliverable per the README:
  1. A `Contact` shape you can defend (dict-based).
  2. A `Roster` skeleton with the email/phone indices.
  3. A `load_csv` that normalizes on read (auto-detect comma vs
     semicolon, trim whitespace, lowercase emails, phone digits only).
  4. `cmd_list` working end-to-end.
The other subcommands are stubbed to exit 1 (Day 2's work).
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path


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
        if row is None:
            continue
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


def cmd_list(args: argparse.Namespace) -> int:
    contacts = load_csv(Path(args.path))
    roster = Roster(contacts)
    for c in roster.sorted_by_name():
        print(f"{c['name']:<24}  {c['email']:<28}  {c['phone']}")
    print(f"({len(contacts)} contacts)", file=sys.stderr)
    return 0


def cmd_find(args: argparse.Namespace) -> int:
    print("(find: not implemented yet)", file=sys.stderr)
    return 1


def cmd_dupes(args: argparse.Namespace) -> int:
    print("(dupes: not implemented yet)", file=sys.stderr)
    return 1


def cmd_export(args: argparse.Namespace) -> int:
    print("(export: not implemented yet)", file=sys.stderr)
    return 1


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
