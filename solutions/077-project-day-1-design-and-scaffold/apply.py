"""Rung 5: Apply.

Use `make_log_text` (rung 4) + `parse_line` (rung 3) together. Print
a tiny summary: total parsed, total skipped (malformed), counts per level.

This is the seed of tomorrow's aggregator.

Try it: uv run python 05_apply.py
"""
from collections import Counter
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_solo_spec = spec_from_file_location(
    "_solo", Path(__file__).parent / "04_solo.py"
)
_solo = module_from_spec(_solo_spec)
_solo_spec.loader.exec_module(_solo)

_parser_spec = spec_from_file_location(
    "_parser", Path(__file__).parent / "03_guided.py"
)
_parser = module_from_spec(_parser_spec)
_parser_spec.loader.exec_module(_parser)


def main() -> None:
    text = _solo.make_log_text(1000, error_rate=0.15, seed=7)
    parsed = 0
    skipped = 0
    levels: Counter = Counter()
    for line in text.splitlines():
        try:
            rec = _parser.parse_line(line)
        except _parser.MalformedLine:
            skipped += 1
            continue
        parsed += 1
        levels[rec.level] += 1

    print(f"parsed:  {parsed}")
    print(f"skipped: {skipped}")
    for level, count in sorted(levels.items()):
        print(f"  {level:<6}: {count}")


if __name__ == "__main__":
    main()
