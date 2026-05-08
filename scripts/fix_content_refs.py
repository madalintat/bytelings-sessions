"""One-shot content-reference fix-up for v1→v2 migration.

The migration script (scripts/migrate_v1_to_v2.py) renamed files but
not the strings *inside* those files. Test files still reference
`"02_fluency.py"` in their spec_from_file_location calls, breaking
imports on the new layout.

This script walks curriculum/ + solutions/ recursively and rewrites
the literal string references. Idempotent — the second-pass replaces
are no-ops.

Mappings:
    "02_fluency.py"      → "fluency.py"
    "02_fluency_test.py" → "fluency_test.py"
    "03_guided.py"       → "guided.py"
    "03_guided_test.py"  → "guided_test.py"
    "04_solo.py"         → "solo.py"
    "04_solo_test.py"    → "solo_test.py"
    "05_apply.py"        → "apply.py"
    "concept.md"         → "README.md"

Plus the file-internal docstring/comment forms like ``open `02_fluency.py```
that show up in CONCEPT_PLACEHOLDER-derived READMEs.

Usage:
    uv run python scripts/fix_content_refs.py [ROOT]

ROOT defaults to current working directory. Operates on
ROOT/curriculum/ and ROOT/solutions/ if those exist.
"""
from __future__ import annotations

import sys
from pathlib import Path

REPLACEMENTS = [
    ('"02_fluency.py"', '"fluency.py"'),
    ('"02_fluency_test.py"', '"fluency_test.py"'),
    ('"03_guided.py"', '"guided.py"'),
    ('"03_guided_test.py"', '"guided_test.py"'),
    ('"04_solo.py"', '"solo.py"'),
    ('"04_solo_test.py"', '"solo_test.py"'),
    ('"05_apply.py"', '"apply.py"'),
    ('"concept.md"', '"README.md"'),
    # Markdown / docstring backtick forms.
    ("`02_fluency.py`", "`fluency.py`"),
    ("`02_fluency_test.py`", "`fluency_test.py`"),
    ("`03_guided.py`", "`guided.py`"),
    ("`03_guided_test.py`", "`guided_test.py`"),
    ("`04_solo.py`", "`solo.py`"),
    ("`04_solo_test.py`", "`solo_test.py`"),
    ("`05_apply.py`", "`apply.py`"),
    ("`concept.md`", "`README.md`"),
    # `try:` example lines like `Try: uv run python 05_apply.py` (no quotes/backticks).
    (" 02_fluency.py", " fluency.py"),
    (" 03_guided.py", " guided.py"),
    (" 04_solo.py", " solo.py"),
    (" 05_apply.py", " apply.py"),
]

WALKABLE_SUFFIXES = {".py", ".md"}


def fix_file(path: Path) -> bool:
    """Rewrite path content. Return True if file was modified."""
    text = path.read_text()
    new = text
    for old, replacement in REPLACEMENTS:
        new = new.replace(old, replacement)
    if new != text:
        path.write_text(new)
        return True
    return False


def run(root: Path) -> int:
    changed = 0
    for top in ("curriculum", "solutions"):
        base = root / top
        if not base.is_dir():
            continue
        for path in base.rglob("*"):
            if path.suffix in WALKABLE_SUFFIXES and path.is_file():
                if fix_file(path):
                    changed += 1
    return changed


def main() -> None:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    changed = run(root)
    print(f"Updated {changed} file(s) in {root}/curriculum and {root}/solutions.")


if __name__ == "__main__":
    main()
