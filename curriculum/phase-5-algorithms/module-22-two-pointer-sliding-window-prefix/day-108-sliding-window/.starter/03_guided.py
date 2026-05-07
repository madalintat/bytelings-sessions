"""Rung 3: Guided — variable-size sliding window.

Topic: longest substring without repeating characters.

Given a string s, return the length of the longest substring with
all-distinct characters.

>>> longest_unique("abcabcbb")
3
>>> longest_unique("bbbbb")
1
>>> longest_unique("pwwkew")
3
>>> longest_unique("")
0

Hints (the standard pattern):
- left = 0; seen = {} (char -> latest index)
- for right, ch in enumerate(s):
    if ch is in seen and seen[ch] >= left:
        left = seen[ch] + 1     # jump past the previous occurrence
    seen[ch] = right
    update best = max(best, right - left + 1)
- O(n), single pass. left only moves forward.
"""


def longest_unique(s: str) -> int:
    raise NotImplementedError
