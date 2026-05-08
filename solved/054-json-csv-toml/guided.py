"""Rung 3: Guided — solved version.

`csv.DictReader` maps each row to a dict keyed by the header row.
Opening with `newline=""` is the recommended practice for csv (so the
module handles universal newlines itself). We convert `id` to int and
skip rows where the conversion fails.
"""
import csv
from pathlib import Path


def load_users(path: Path) -> list[dict]:
    users = []
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            try:
                users.append({"id": int(row["id"]), "name": row["name"]})
            except (ValueError, KeyError):
                continue
    return users
