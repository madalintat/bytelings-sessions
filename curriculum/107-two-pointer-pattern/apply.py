"""Rung 5: Apply — palindrome checker via two pointers.

Try it: uv run python apply.py

Patterns: P-08 (two-pointer-from-ends), P-09 (two-pointer-fast-slow).
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location(
    "_solo", Path(__file__).parent / "solo.py"
)
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def is_palindrome(s: str) -> bool:
    """Two-pointer palindrome check, ignoring non-letters and case."""
    s = "".join(c.lower() for c in s if c.isalnum())
    lo, hi = 0, len(s) - 1
    while lo < hi:
        if s[lo] != s[hi]:
            return False
        lo += 1
        hi -= 1
    return True


def main() -> None:
    cases = ["racecar", "hello", "A man, a plan, a canal: Panama", "", "a"]
    for c in cases:
        print(f"  {c!r:>40} -> {is_palindrome(c)}")

    arr = [1, 1, 2, 2, 3, 4, 4, 5]
    k = _solo.remove_duplicates(arr)
    print(f"\nremove_duplicates -> {k} unique: {arr[:k]}")


if __name__ == "__main__":
    main()
