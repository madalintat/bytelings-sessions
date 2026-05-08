"""Rung 3: Guided — solved version.

`src.with_suffix(new_ext)` creates a sibling path with a different
extension — cleaner than string manipulation. `src.read_text()` and
`dest.write_text(content)` handle open/close automatically.
"""
from pathlib import Path


def swap_extension(src: Path, new_ext: str) -> Path:
    content = src.read_text()
    dest = src.with_suffix(new_ext)
    dest.write_text(content)
    return dest
