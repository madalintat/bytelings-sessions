"""Rung 4: Solo — solved version.

Two-pointer sweep on sorted arrivals and departures.

The key insight: at each moment, process the next event (either an arrival
or a departure). An arrival needs a new platform; a departure frees one.
When an arrival and departure happen at the same time, process the departure
first — that platform can be reused for the new arrival (no wait).

Time: O(n log n) for sorting + O(n) scan = O(n log n) total.
Space: O(n) for the sorted copies (O(1) if sorted in-place).
"""


def min_platforms(arrivals: list[int], departures: list[int]) -> int:
    """Return the minimum number of platforms so no train waits."""
    arr = sorted(arrivals)
    dep = sorted(departures)

    platforms = 0   # current platforms in use
    max_platforms = 0
    i = 0           # pointer into arrivals
    j = 0           # pointer into departures

    while i < len(arr):
        if arr[i] < dep[j]:
            # Next event is an arrival — need one more platform.
            platforms += 1
            max_platforms = max(max_platforms, platforms)
            i += 1
        else:
            # Next event is a departure — free a platform.
            platforms -= 1
            j += 1

    return max_platforms
