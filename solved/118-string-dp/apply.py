"""Rung 5: Apply — solved version.

segment() uses @functools.cache on an inner solve(i) that returns
list[str] | None. At each position, try every matching word; if the
tail recursion succeeds, prepend the word and return. Cache the result
so repeated suffixes are resolved in O(1).

Pattern: P-28 (memoize-recursive)
"""
import functools
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location("_solo", Path(__file__).parent / "solo.py")
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def segment(s: str, words: list[str]) -> list[str] | None:
    word_set = set(words)

    @functools.cache
    def solve(i: int) -> list[str] | None:
        if i == len(s):
            return []  # base case: empty suffix segmented successfully
        for word in word_set:
            end = i + len(word)
            if s[i:end] == word:
                tail = solve(end)
                if tail is not None:
                    return [word] + tail  # prepend — builds left-to-right
        return None  # no word matches here

    return solve(0)


def main() -> None:
    result = segment("applepenapple", ["apple", "pen"])
    assert result == ["apple", "pen", "apple"], (
        f"Expected ['apple', 'pen', 'apple'], got {result!r}"
    )
    print(f"segment('applepenapple', ...) = {result} ✓")

    result2 = segment("catsandog", ["cats", "dog", "sand", "and", "cat"])
    assert result2 is None, f"Expected None, got {result2!r}"
    print(f"segment('catsandog', ...) = {result2} ✓")

    result3 = segment("pineapplepenapple", ["pine", "apple", "pen", "pineapple"])
    assert result3 is not None and "".join(result3) == "pineapplepenapple"
    print(f"segment('pineapplepenapple', ...) = {result3} ✓")

    assert _solo.can_break("leetcode", ["leet", "code"]) is True
    print("can_break sanity check ✓")

    print("\n✓ apply.py complete")


if __name__ == "__main__":
    main()
