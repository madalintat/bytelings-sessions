"""Rung 3: Guided implement — solved version.

Pre-compute the state sequence once (O(n) transitions total), then
binary-search for the first index where is_ok fails. This keeps
the is_ok call count to O(log n) in the worst case.
"""
from typing import Any, Callable


def bisect_failures(
    start_state: Any,
    changes: list[Callable[[Any], Any]],
    is_ok: Callable[[Any], bool],
) -> int | None:
    """Return the index of the first change that breaks `is_ok`."""
    if not changes:
        return None

    # Build the state sequence: states[k] is state after applying changes[:k].
    states = [start_state]
    for fn in changes:
        states.append(fn(states[-1]))

    # Binary search: find smallest k > 0 where not is_ok(states[k]).
    lo, hi = 1, len(changes)
    # First confirm there is a failure at all.
    if is_ok(states[hi]):
        return None

    while lo < hi:
        mid = (lo + hi) // 2
        if is_ok(states[mid]):
            lo = mid + 1
        else:
            hi = mid

    return lo - 1  # 0-based index into changes
