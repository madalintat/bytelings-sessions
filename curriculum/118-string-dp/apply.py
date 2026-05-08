"""Rung 5: Apply — segment a string into words, return one valid split.

Pattern: P-28 (memoize-recursive)

Implement `segment(s, words) -> list[str] | None` that returns ONE valid
segmentation of s (a list of words), or None if no segmentation exists.

Use memoization — same pattern as can_break but track the chosen word
at each position so the path can be reconstructed.

Run with: uv run python curriculum/118-string-dp/apply.py
"""
import functools
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location("_solo", Path(__file__).parent / "solo.py")
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def segment(s: str, words: list[str]) -> list[str] | None:
    """Return one valid segmentation of s, or None if none exists.

    Args:
        s:     the string to segment
        words: available vocabulary (words may be reused)

    Returns:
        A list of strings whose concatenation equals s, all from words.
        None if s cannot be fully segmented.

    Hint:
    - Use @functools.cache on an inner solve(i) that returns
      list[str] | None.
    - At each position i, try every word that matches s[i:i+len(word)].
      If solve(i + len(word)) succeeds, prepend word and return.
    - Base case: solve(len(s)) returns [].
    - Memoize so repeated suffixes are only solved once.
    """
    word_set = set(words)

    # TODO: implement with @functools.cache
    raise NotImplementedError


def main() -> None:
    # Basic correctness
    result = segment("applepenapple", ["apple", "pen"])
    assert result == ["apple", "pen", "apple"], (
        f"Expected ['apple', 'pen', 'apple'], got {result!r}"
    )
    print(f"segment('applepenapple', ...) = {result} ✓")

    # Should return None
    result2 = segment("catsandog", ["cats", "dog", "sand", "and", "cat"])
    assert result2 is None, f"Expected None, got {result2!r}"
    print(f"segment('catsandog', ...) = {result2} ✓")

    # Longer example
    result3 = segment("pineapplepenapple", ["pine", "apple", "pen", "pineapple"])
    assert result3 is not None and "".join(result3) == "pineapplepenapple"
    print(f"segment('pineapplepenapple', ...) = {result3} ✓")

    # Verify can_break is consistent
    assert _solo.can_break("leetcode", ["leet", "code"]) is True
    print("can_break sanity check ✓")

    print("\n✓ apply.py complete")


if __name__ == "__main__":
    main()
