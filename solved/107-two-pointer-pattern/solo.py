"""Rung 4: Solo — solved version.

Fast/slow two-pointer (P-09). `slow` always points at the last
position written; `fast` scans forward. When `fast` finds a value
different from `slow`'s value, that value is unique-so-far. Advance
`slow`, copy the new value, continue.

The empty-array edge case returns 0 because the `for fast in
range(1, len(arr))` loop never enters and `slow` stays at -1, so we
guard with `if not arr: return 0` upfront.

Why fast starts at 1 (not 0): position 0 is always the first unique
by definition, so `slow` starts at 0 (already counts as unique-so-
far) and we scan from index 1 onward.
"""


def remove_duplicates(arr: list[int]) -> int:
    if not arr:
        return 0
    slow = 0
    for fast in range(1, len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]
    return slow + 1
