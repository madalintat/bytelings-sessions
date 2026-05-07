"""Contacts Manager — Day 3: tested, polished, shipped.

A small CLI for loading messy contact CSVs, searching, finding
duplicates, and exporting clean data.

Big-O quick map:
    list:        O(n log n) — sort by name
    find email:  O(1) via by_email index
    find phone:  O(1) via by_phone index
    find regex:  O(n) — must scan all names
    dupes:       O(n) — single pass + defaultdict grouping
    export:      O(n)

The slowest path users hit is `find --regex`, which is linear. For a
roster of 50k that's still well under a second on commodity hardware,
so we accept it.
"""
from __future__ import annotations

import functools
import re
import sys
import time
from collections import defaultdict
from pathlib import Path
from typing import Callable


BANNER = "contacts — a small CLI for messy address books"


# --- Domain helpers -----------------------------------------------------------

def normalize_phone(raw: str) -> str:
    return "".join(c for c in raw if c.isdigit())


def normalize_email(raw: str) -> str:
    return raw.strip().lower()


def normalize_name(raw: str) -> str:
    return " ".join(raw.split())


def detect_separator(header_line: str) -> str:
    return ";" if header_line.count(";") > header_line.count(",") else ","


def load_csv(path: str | Path) -> list[dict[str, str]]:
    """Read a contacts CSV and return a list of normalized dicts."""
    text = Path(path).read_text(encoding="utf-8")
    lines = [ln for ln in text.splitlines() if ln.strip()]
    if not lines:
        return []
    sep = detect_separator(lines[0])
    header = [h.strip().lower() for h in lines[0].split(sep)]
    contacts: list[dict[str, str]] = []
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


# --- The @timed decorator -----------------------------------------------------

def timed(fn: Callable) -> Callable:
    """Print elapsed ms to stderr after the wrapped call."""
    @functools.wraps(fn)
    def wrapped(*args, **kwargs):
        t0 = time.perf_counter()
        try:
            return fn(*args, **kwargs)
        finally:
            elapsed_ms = (time.perf_counter() - t0) * 1000
            print(f"[timed] {fn.__name__}: {elapsed_ms:.2f}ms", file=sys.stderr)
    return wrapped


# --- Roster -------------------------------------------------------------------

class Roster:
    def __init__(self, contacts: list[dict]) -> None:
        self.contacts = contacts
        self.by_email = {c["email"]: c for c in contacts if c["email"]}
        self.by_phone = {c["phone"]: c for c in contacts if c["phone"]}

    def names_sorted(self) -> list[str]:
        return sorted(c["name"] for c in self.contacts)

    def find_by_email(self, email: str) -> dict | None:
        return self.by_email.get(normalize_email(email))

    def find_by_phone(self, phone: str) -> dict | None:
        return self.by_phone.get(normalize_phone(phone))

    def find_by_regex(self, pattern: str) -> list[dict]:
        try:
            rx = re.compile(pattern)
        except re.error as e:
            raise ValueError(f"bad regex: {e}") from e
        return [c for c in self.contacts if rx.search(c["name"])]


# --- Dupes --------------------------------------------------------------------

def dupe_key(c: dict) -> tuple[str, str]:
    initials = "".join(p[:1] for p in c["name"].lower().split() if p)
    return (initials, c["phone"])


def find_dupes(contacts: list[dict]) -> list[list[dict]]:
    groups: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for c in contacts:
        if not c["phone"]:
            continue
        groups[dupe_key(c)].append(c)
    clusters = [g for g in groups.values() if len(g) > 1]
    # Deterministic order: sort each cluster by name, then sort clusters
    # by their first member's name.
    for g in clusters:
        g.sort(key=lambda c: c["name"])
    clusters.sort(key=lambda g: g[0]["name"])
    return clusters


# --- Export -------------------------------------------------------------------

def export_csv(contacts: list[dict], path: str | Path) -> None:
    lines = ["name,email,phone"]
    for c in contacts:
        lines.append(f"{c['name']},{c['email']},{c['phone']}")
    Path(path).write_text("\n".join(lines) + "\n", encoding="utf-8")


# --- Commands -----------------------------------------------------------------

def cmd_list(roster: Roster) -> int:
    for name in roster.names_sorted():
        print(name)
    print(f"({len(roster.contacts)} contacts)", file=sys.stderr)
    return 0


@timed
def cmd_find(roster: Roster, args: list[str]) -> int:
    if len(args) != 2:
        print("usage: find <csv> --email|--phone|--regex <value>", file=sys.stderr)
        return 2
    flag, value = args
    if flag == "--email":
        c = roster.find_by_email(value)
        if c is None:
            return 1
        print(f"{c['name']},{c['email']},{c['phone']}")
        return 0
    if flag == "--phone":
        c = roster.find_by_phone(value)
        if c is None:
            return 1
        print(f"{c['name']},{c['email']},{c['phone']}")
        return 0
    if flag == "--regex":
        try:
            results = roster.find_by_regex(value)
        except ValueError as e:
            print(f"error: {e}", file=sys.stderr)
            return 2
        if not results:
            return 1
        for c in results:
            print(f"{c['name']},{c['email']},{c['phone']}")
        return 0
    print(f"unknown flag: {flag}", file=sys.stderr)
    return 2


@timed
def cmd_dupes(roster: Roster) -> int:
    clusters = find_dupes(roster.contacts)
    if not clusters:
        print("(no duplicates)")
        return 0
    for i, cluster in enumerate(clusters, start=1):
        print(f"# group {i}")
        for c in cluster:
            print(f"  {c['name']} | {c['email']} | {c['phone']}")
    return 0


def cmd_export(roster: Roster, out_path: str) -> int:
    export_csv(roster.contacts, out_path)
    print(f"wrote {len(roster.contacts)} contacts to {out_path}")
    return 0


# --- CLI plumbing -------------------------------------------------------------

USAGE = f"""\
{BANNER}

usage: app.py <command> [args]
commands:
  list   <csv>                                  print all names sorted
  find   <csv> --email|--phone|--regex <value>  search
  dupes  <csv>                                  show duplicate clusters
  export <csv> <out>                            export normalized CSV
  --help                                        show this help
"""


def main(argv: list[str]) -> int:
    if len(argv) < 2 or argv[1] in ("--help", "-h", "help"):
        print(USAGE, file=sys.stderr)
        return 0 if len(argv) >= 2 and argv[1] in ("--help", "-h", "help") else 2
    if len(argv) < 3:
        print(USAGE, file=sys.stderr)
        return 2
    command, csv_path, *rest = argv[1:]
    csv_p = Path(csv_path)
    if not csv_p.exists():
        print(f"error: file not found: {csv_path}", file=sys.stderr)
        return 2
    try:
        contacts = load_csv(csv_p)
    except OSError as e:
        print(f"error: cannot read {csv_path}: {e}", file=sys.stderr)
        return 2
    roster = Roster(contacts)
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
