"""Rung 3: Guided implement.

Topic: read CSV with DictReader, return a typed list

Implement `load_users(path)`:
- `path` is a Path to a CSV file with a header row containing
  at least 'id' and 'name'.
- Return a list of dicts: [{'id': int, 'name': str}, ...]
- The 'id' column is a string in the CSV; convert it to int.
- Skip rows where 'id' isn't a valid integer.

Use csv.DictReader.
"""
import csv
from pathlib import Path


def load_users(path: Path) -> list[dict]:
    # TODO: open the file (newline="" recommended), wrap in DictReader,
    #       build [{'id': int(row['id']), 'name': row['name']}] skipping bad rows.
    raise NotImplementedError
