"""Rung 4: Solo implement. No scaffold beyond the spec.

Topic: a small file utility

Implement `largest_file(folder)`:
- `folder` is a Path to a directory.
- Recursively scan all files under `folder` (use rglob('*')).
- Skip directories — only count regular files.
- Return the Path of the file with the largest size in bytes.
- If there are no files, return None.
- Ties: return the first one encountered.

Constraints:
- Use pathlib only; no os.walk.
- Don't load any file content — only stat sizes.

The tests in 04_solo_test.py are HIDDEN. Don't peek before you try.
"""
from pathlib import Path


def largest_file(folder: Path) -> Path | None:
    raise NotImplementedError
