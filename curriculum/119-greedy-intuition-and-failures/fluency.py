"""Rung 2: Fluency drill — fix the greedy meeting picker.

Topic: classic greedy — activity selection.

Each meeting is (start, end). You can attend at most one meeting at
a time. Return the maximum number of non-overlapping meetings you can
attend.

The classic greedy: sort by EARLIEST END TIME, then pick each meeting
whose start is >= the end of the last picked meeting.

`max_meetings` is sorting by start time — wrong sort. Fix it.
"""


def max_meetings(meetings: list[tuple[int, int]]) -> int:
    if not meetings:
        return 0
    # TODO: sort by end time, not start time.
    sorted_m = sorted(meetings, key=lambda m: m[0])
    count = 0
    last_end = float("-inf")
    for start, end in sorted_m:
        if start >= last_end:
            count += 1
            last_end = end
    return count
