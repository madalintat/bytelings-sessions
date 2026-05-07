"""Rung 3: Guided implement.

Topic: read + write text via Path

Implement `swap_extension(src, new_ext)`:
- `src` is a Path to an existing text file.
- `new_ext` is a string starting with a dot, e.g. ".bak".
- Read the contents of `src`.
- Write them to a sibling file with the same stem but the new
  extension. (Use src.with_suffix(new_ext).)
- Return the new Path.

Example:
    swap_extension(Path("/tmp/notes.txt"), ".bak")
    # → reads /tmp/notes.txt, writes /tmp/notes.bak with the same content
    # → returns Path("/tmp/notes.bak")
"""
from pathlib import Path


def swap_extension(src: Path, new_ext: str) -> Path:
    # TODO: src.read_text(); compute new path with .with_suffix; write it; return it.
    raise NotImplementedError
