"""Rung 2: Fluency — solved version.

Maintain `running` as the current window's sum. Subtract the
outgoing element and add the incoming one each step. O(n) total
instead of O(n*k).

The `running = sum(arr[:k])` initialization computes the FIRST
window in O(k) once; thereafter each step is O(1).
"""


def window_sums(arr: list[int], k: int) -> list[int]:
    if k > len(arr) or k <= 0:
        return []
    running = sum(arr[:k])
    out = [running]
    for i in range(k, len(arr)):
        running += arr[i] - arr[i - k]
        out.append(running)
    return out
