"""Rung 3: Guided — solved version.

Iterating the file object directly (`for line in f`) streams one line
at a time without loading the whole file into memory. The `sum()` with
a conditional generator counts matching lines without building an
intermediate list.
"""
from pathlib import Path


def count_matching_lines(path: Path, needle: str) -> int:
    count = 0
    with open(path, encoding="utf-8") as f:
        for line in f:
            if needle in line:
                count += 1
    return count
