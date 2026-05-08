"""Rung 3: Guided — solved version.

Counting subarrays with sum k via prefix-sum hashing. Insight: a
subarray arr[i..j] sums to k iff prefix_sum[j+1] - prefix_sum[i] ==
k. So at each j, count how many earlier prefix sums equal
running_sum - k.

`seen` starts with {0: 1} for the empty prefix — handles the case
where arr[0..j] itself sums to k (i.e. i = 0).

O(n) time, O(n) space. Works with negative numbers (which kills the
sliding-window approach for similar-sounding problems).
"""


def count_subarrays_with_sum(arr: list[int], k: int) -> int:
    seen: dict[int, int] = {0: 1}
    running = 0
    answer = 0
    for x in arr:
        running += x
        answer += seen.get(running - k, 0)
        seen[running] = seen.get(running, 0) + 1
    return answer
