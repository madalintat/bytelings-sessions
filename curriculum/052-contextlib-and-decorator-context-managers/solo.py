"""Rung 4: Solo implement. No scaffold beyond the spec.

Topic: open many files with ExitStack

Implement `read_all_lines(paths)`:
- Open every path in `paths` for reading.
- Use `contextlib.ExitStack` so all files get closed at the end, even
  if one of the opens fails partway through.
- Return a flat list of all lines (with trailing newlines stripped)
  from all files, in path order then line order.
- If `paths` is empty, return [].

Constraints:
- You must use ExitStack, not nested `with` statements.
- The returned list must NOT contain the trailing "\n".

The tests in 04_solo_test.py are HIDDEN. Don't peek before you try.

Patterns: P-19 (context-manager-protocol).
"""
from contextlib import ExitStack


def read_all_lines(paths: list) -> list[str]:
    raise NotImplementedError
