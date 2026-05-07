"""Rung 5: Apply.

Tiny CLI: read lines from stdin, print which ones are palindromes.

Reuses is_palindrome from rung 4.

Try it: printf "racecar\nhello\nA man, a plan, a canal: Panama\n" | uv run python 05_apply.py
"""
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location(
    "_solo", Path(__file__).parent / "04_solo.py"
)
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def main() -> None:
    for line in sys.stdin:
        line = line.rstrip("\n")
        if not line:
            continue
        verdict = "yes" if _solo.is_palindrome(line) else "no"
        print(f"{verdict}: {line}")


if __name__ == "__main__":
    main()
