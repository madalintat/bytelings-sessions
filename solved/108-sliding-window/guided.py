"""Rung 3: Guided — solved version.

Variable-size window. `seen` maps each character to its most recent
index. When we encounter a repeated character whose previous index
is INSIDE the current window (>= left), jump `left` past that index.
Then update `seen[ch]` and bump `best`.

The `seen[ch] >= left` guard is the key: characters that appeared
BEFORE the current window's left edge are no longer in the window
and don't trigger a jump.

O(n) single pass; left only moves forward (never resets to 0).
"""


def longest_unique(s: str) -> int:
    seen: dict[str, int] = {}
    left = 0
    best = 0
    for right, ch in enumerate(s):
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1
        seen[ch] = right
        best = max(best, right - left + 1)
    return best
