"""Rung 4: Solo.

Topic: longest common subsequence (LCS).

Given two strings a and b, return the length of the longest sequence
of characters that appears in both, in order, but not necessarily
contiguous.

>>> lcs_length("abcde", "ace")
3      # "ace"
>>> lcs_length("abc", "def")
0
>>> lcs_length("abc", "")
0

Recurrence (classic 2D DP):
- dp[i][j] = LCS length of a[:i] and b[:j].
- If a[i-1] == b[j-1]: dp[i][j] = dp[i-1][j-1] + 1
- Else:                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
- Base: row 0 and col 0 are 0 (empty prefix has LCS 0 with anything).

Tests in 04_solo_test.py are HIDDEN.
"""


def lcs_length(a: str, b: str) -> int:
    raise NotImplementedError
