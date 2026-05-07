"""Contacts Manager — Day 1 skeleton.

Big-O note (fill this in by end of day 3):
    * load        — O(n) one-pass parse over rows
    * list        — O(n log n) sorted by name
    * find/dupes  — fill in tomorrow

CLI:
    python app.py list <csv>
    python app.py find  ...    (Day 2)
    python app.py dupes ...    (Day 2)
    python app.py export ...   (Day 2)
"""
from __future__ import annotations

import sys
from pathlib import Path


# --- Domain helpers -----------------------------------------------------------

def normalize_phone(raw: str) -> str:
    """Strip a phone number to digits only.

    >>> normalize_phone('(415) 555-1212')
    '4155551212'
    >>> normalize_phone('+1 415 555-0104')
    '14155550104'
    >>> normalize_phone('')
    ''
    """
    return "".join(c for c in raw if c.isdigit())


def normalize_email(raw: str) -> str:
    """Lowercase + strip whitespace."""
    return raw.strip().lower()


def normalize_name(raw: str) -> str:
    """Strip + collapse internal whitespace; keep original casing."""
    return " ".join(raw.split())


# --- Loader -------------------------------------------------------------------

def detect_separator(header_line: str) -> str:
    """Return ';' if the header has more semicolons than commas, else ','."""
    return ";" if header_line.count(";") > header_line.count(",") else ","


def load_csv(path: str | Path) -> list[dict[str, str]]:
    """Read a contacts CSV and return a list of normalized dicts.

    Each dict has keys 'name', 'email', 'phone' (always present, possibly '').
    The first row is a header; column order doesn't matter as long as those
    three names appear.

    Lines that don't have the expected number of fields are skipped silently.
    """
    text = Path(path).read_text(encoding="utf-8")
    lines = [ln for ln in text.splitlines() if ln.strip()]
    if not lines:
        return []
    sep = detect_separator(lines[0])
    header = [h.strip().lower() for h in lines[0].split(sep)]
    contacts = []
    for line in lines[1:]:
        parts = [p.strip() for p in line.split(sep)]
        if len(parts) != len(header):
            continue
        record = dict(zip(header, parts))
        contacts.append({
            "name": normalize_name(record.get("name", "")),
            "email": normalize_email(record.get("email", "")),
            "phone": normalize_phone(record.get("phone", "")),
        })
    return contacts


# --- Roster -------------------------------------------------------------------

class Roster:
    """In-memory contacts roster with two indices."""

    def __init__(self, contacts: list[dict]) -> None:
        self.contacts = contacts
        self.by_email = {c["email"]: c for c in contacts if c["email"]}
        self.by_phone = {c["phone"]: c for c in contacts if c["phone"]}

    def names_sorted(self) -> list[str]:
        return sorted(c["name"] for c in self.contacts)


# --- Commands -----------------------------------------------------------------

def cmd_list(roster: Roster) -> int:
    for name in roster.names_sorted():
        print(name)
    return 0


def cmd_find(roster: Roster, args: list[str]) -> int:
    print("(not implemented yet — see Day 2)", file=sys.stderr)
    return 1


def cmd_dupes(roster: Roster) -> int:
    print("(not implemented yet — see Day 2)", file=sys.stderr)
    return 1


def cmd_export(roster: Roster, out_path: str) -> int:
    print("(not implemented yet — see Day 2)", file=sys.stderr)
    return 1


# --- CLI plumbing -------------------------------------------------------------

USAGE = """\
usage: app.py <command> [args]
commands:
  list   <csv>                 print all names sorted
  find   <csv> --email|--regex <value>     (Day 2)
  dupes  <csv>                 (Day 2)
  export <csv> <out>           (Day 2)
"""


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print(USAGE, file=sys.stderr)
        return 2
    command, csv_path, *rest = argv[1:]
    if not Path(csv_path).exists():
        print(f"error: file not found: {csv_path}", file=sys.stderr)
        return 2
    roster = Roster(load_csv(csv_path))
    if command == "list":
        return cmd_list(roster)
    if command == "find":
        return cmd_find(roster, rest)
    if command == "dupes":
        return cmd_dupes(roster)
    if command == "export":
        if not rest:
            print("error: export requires an output path", file=sys.stderr)
            return 2
        return cmd_export(roster, rest[0])
    print(f"unknown command: {command}", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
