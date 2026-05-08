"""Rung 3: Guided — count decode ways.

Topic: string DP — number of ways to decode.

A message uses A=1, B=2, ..., Z=26. Given a string of digits, return
how many distinct ways it can be decoded.

>>> num_decodings("12")
2     # "AB" (1, 2) or "L" (12)
>>> num_decodings("226")
3     # "BBF" (2,2,6); "BZ" (2,26); "VF" (22,6)
>>> num_decodings("0")
0     # 0 has no letter
>>> num_decodings("06")
0     # leading zero is invalid
>>> num_decodings("")
1     # empty string decodes one way (vacuously)

Hints:
- dp[i] = number of ways to decode s[i:].
- Base: dp[len(s)] = 1.
- s[i] == "0" → dp[i] = 0 (no letter starts with 0).
- Otherwise dp[i] = dp[i+1] + (dp[i+2] if 10 <= int(s[i:i+2]) <= 26 else 0).
- Either bottom-up array or top-down with @cache(maxsize=None).
"""


def num_decodings(s: str) -> int:
    raise NotImplementedError
