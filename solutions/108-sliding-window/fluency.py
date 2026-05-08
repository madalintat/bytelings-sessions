"""Rung 2: Fluency drill — replace O(nk) with O(n) sliding window.

Topic: don't recompute the whole window each step.

`window_sums` is correct but slow — it sums every window from scratch.
Rewrite so each step adds the new element and subtracts the old one.

Returns a list of length len(arr) - k + 1 (or [] if k > len(arr)).
"""


def window_sums(arr: list[int], k: int) -> list[int]:
    if k > len(arr) or k <= 0:
        return []
    # TODO: this is O(n*k). Make it O(n) by sliding.
    out = []
    for i in range(len(arr) - k + 1):
        out.append(sum(arr[i:i + k]))
    return out
