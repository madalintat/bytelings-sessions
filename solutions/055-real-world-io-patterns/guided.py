"""Rung 3: Guided implement.

Topic: streaming a large file line-by-line

Implement `count_matching_lines(path, needle)`:
- `path` is a Path to a (possibly large) text file.
- `needle` is a string.
- Return the number of lines containing `needle` as a substring.

Constraints:
- Stream the file. Do NOT do `path.read_text().splitlines()`.
- Use a `with open(...)` block, encoding="utf-8".
- Iterate the file object directly (`for line in f`).
"""
from pathlib import Path


def count_matching_lines(path: Path, needle: str) -> int:
    # TODO: open with utf-8 encoding, iterate file lazily, count matches.
    raise NotImplementedError
