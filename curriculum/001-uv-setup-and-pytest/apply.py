"""Rung 5: Apply.

Tiny CLI: read a sentence from stdin and print the vowel count.

This uses count_vowels from rung 4 — your first reuse of your own code.

Try it: echo "hello world" | uv run python apply.py

Patterns: P-01 (sentinel-loop).
"""
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location(
    "_solo", Path(__file__).parent / "solo.py"
)
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def main() -> None:
    text = sys.stdin.read().strip()
    if not text:
        print("(no input)")
        return
    n = _solo.count_vowels(text)
    print(f"{n} vowel{'s' if n != 1 else ''} in: {text!r}")


if __name__ == "__main__":
    main()
