"""Rung 5: Apply.

CLI: read text from stdin, print the top N words, ranked.

Try it:
  echo "the quick brown fox the lazy dog the" | uv run python apply.py 2
"""
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location("_solo", Path(__file__).parent / "solo.py")
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def main(argv: list[str]) -> int:
    n = int(argv[1]) if len(argv) > 1 else 5
    text = sys.stdin.read()
    for word, count in _solo.top_words(text, n):
        print(f"{count:>6} {word}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
