"""Rung 5: Apply.

Print the longest palindrome inside each of a few real-ish strings.

Try it: uv run python 05_apply.py
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location(
    "_solo", Path(__file__).parent / "04_solo.py"
)
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def main() -> None:
    samples = [
        "racecarsRcoolBUTbobistoo",
        "level up your engineering",
        "anna and madam went home",
        "no palindromes here longer than one",
    ]
    for s in samples:
        out = _solo.longest_palindrome(s)
        print(f"  {s!r}\n    longest palindrome: {out!r} (len {len(out)})")


if __name__ == "__main__":
    main()
