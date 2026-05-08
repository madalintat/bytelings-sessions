"""Sync each curriculum README's frontmatter to match its current
folder slug + module assignment from info.toml.

After M6/M11 rotations the READMEs were moved but their YAML
frontmatter (`day:`, `module:`, h1) still pointed at the v1 day number.
This script reads info.toml, walks curriculum/<slug>/README.md, and
rewrites:

  ---
  day: <new slug>
  ...
  module: <new module>
  ...
  ---
  # Day <new number> — <preserved title>

Idempotent: skips files already aligned. Mirrors the change to
solutions/<slug>/README.md if present.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from bytelings import info_toml  # noqa: E402

_FRONTMATTER_RE = re.compile(r"^(---\n.*?\n---\n)(.*)", re.DOTALL)
_DAY_LINE_RE = re.compile(r"^day:\s*.*$", re.MULTILINE)
_MODULE_LINE_RE = re.compile(r"^module:\s*.*$", re.MULTILINE)
_H1_RE = re.compile(r"^#\s+Day\s+\d+\s+—\s+(.*)$", re.MULTILINE)


def _fix_one(path: Path, new_slug: str, day_number: int, new_module: str) -> bool:
    """Rewrite the frontmatter day/module + h1 day-number. Return True if changed."""
    text = path.read_text()
    m = _FRONTMATTER_RE.match(text)
    if not m:
        return False
    fm, body = m.group(1), m.group(2)
    new_fm = _DAY_LINE_RE.sub(f"day: {new_slug}", fm, count=1)
    new_fm = _MODULE_LINE_RE.sub(f"module: {new_module}", new_fm, count=1)

    h1 = _H1_RE.search(body)
    new_body = body
    if h1:
        title = h1.group(1)
        new_body = _H1_RE.sub(f"# Day {day_number} — {title}", body, count=1)

    new = new_fm + new_body
    if new == text:
        return False
    path.write_text(new)
    return True


def run(root: Path) -> tuple[int, int]:
    entries = info_toml.load(root / "curriculum" / "info.toml")
    changed = 0
    skipped = 0
    for e in entries:
        for top in ("curriculum", "solutions"):
            readme = root / top / e.slug / "README.md"
            if not readme.is_file():
                continue
            if _fix_one(readme, e.slug, e.day_number, e.module):
                changed += 1
            else:
                skipped += 1
    return changed, skipped


def main() -> None:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    changed, skipped = run(root)
    print(f"Updated {changed} README(s); {skipped} were already aligned.")


if __name__ == "__main__":
    main()
