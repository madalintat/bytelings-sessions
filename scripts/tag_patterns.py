"""Inject `Patterns: P-NN (name), …` headers into solo/apply rungs.

Source of truth: `bytelings.patterns.PATTERNS`. Each Pattern lists
the day numbers that exercise it. We invert that into
`day_number → [(id, name), …]` and inject a `Patterns:` line into
each matching day's solo.py and apply.py module docstring.

Idempotent: skips files that already carry a `Patterns:` line.
Operates on both curriculum/ and solutions/ (mirror).

Usage:
    uv run python scripts/tag_patterns.py [ROOT]
"""
from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from bytelings import patterns as pat  # noqa: E402
from bytelings import info_toml  # noqa: E402


def _build_index() -> dict[int, list[tuple[str, str]]]:
    """day_number → [(pattern_id, pattern_name), …]"""
    by_day: dict[int, list[tuple[str, str]]] = defaultdict(list)
    for p in pat.PATTERNS:
        for d in p.days:
            by_day[d].append((p.id, p.name))
    # Stable order within each day.
    for d in by_day:
        by_day[d].sort(key=lambda t: t[0])
    return dict(by_day)


_DOCSTRING_END_RE = re.compile(r'(""")\s*$', re.MULTILINE)


def _inject_pattern_line(text: str, line: str) -> str | None:
    """Insert `line` at the end of the module docstring, before its `\"\"\"`.

    Returns new text, or None if injection isn't possible (no docstring,
    or the line is already present).
    """
    if line in text:
        return None
    # Module docstring is the first triple-quoted block. Find its end.
    if not text.lstrip().startswith('"""'):
        return None
    # First closing triple-quote that ends a line.
    first_open = text.index('"""')
    after_open = first_open + 3
    end = text.find('"""', after_open)
    if end == -1:
        return None
    body = text[after_open:end]
    # Insert a blank line + the patterns line at the END of the docstring,
    # immediately before the closing """.
    if body.endswith("\n"):
        new_body = body + f"\n{line}\n"
    else:
        new_body = body + f"\n\n{line}\n"
    return text[:after_open] + new_body + text[end:]


def _format_line(pairs: list[tuple[str, str]]) -> str:
    parts = ", ".join(f"{pid} ({name})" for pid, name in pairs)
    return f"Patterns: {parts}."


def run(root: Path) -> tuple[int, int]:
    """Tag solo.py and apply.py in curriculum/ and solutions/.

    Returns (files_tagged, files_skipped).
    """
    by_day = _build_index()
    entries = info_toml.load(root / "curriculum" / "info.toml")
    if not entries:
        return (0, 0)

    tagged = 0
    skipped = 0
    for entry in entries:
        if entry.day_number not in by_day:
            continue
        pairs = by_day[entry.day_number]
        line = _format_line(pairs)
        for top in ("curriculum", "solutions"):
            base = root / top / entry.slug
            for fname in ("solo.py", "apply.py"):
                target = base / fname
                if not target.is_file():
                    continue
                text = target.read_text()
                new = _inject_pattern_line(text, line)
                if new is None:
                    skipped += 1
                    continue
                target.write_text(new)
                tagged += 1
    return (tagged, skipped)


def main() -> None:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    tagged, skipped = run(root)
    print(f"Tagged {tagged} file(s); skipped {skipped} (already tagged or no docstring).")


if __name__ == "__main__":
    main()
