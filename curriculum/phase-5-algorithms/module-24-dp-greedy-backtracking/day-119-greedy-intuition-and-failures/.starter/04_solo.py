"""Rung 4: Solo.

Topic: jump-game greedy.

Given an array `arr` of non-negative ints, where arr[i] is the
maximum jump length from index i, return True iff you can reach the
last index starting from index 0.

>>> can_jump([2, 3, 1, 1, 4])
True     # 0 -> 1 -> 4
>>> can_jump([3, 2, 1, 0, 4])
False    # gets stuck at index 3
>>> can_jump([0])
True     # already at the last index
>>> can_jump([])
False

Greedy approach (provably correct here):
- Track the FARTHEST index reachable so far.
- Walk i from 0; at each step, if i > farthest, you're stuck → False.
- Otherwise update farthest = max(farthest, i + arr[i]).
- If farthest >= last index, you can reach.
- O(n).

Tests in 04_solo_test.py are HIDDEN.
"""


def can_jump(arr: list[int]) -> bool:
    raise NotImplementedError
