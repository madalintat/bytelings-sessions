"""Rung 3: Guided implement — `bisect_failures`.

Topic: bisecting a sequence of changes to find the first one that
breaks an invariant. (A toy version of `git bisect`, but for any
list of "changes" applied to a state.)

Real-world framing: 32 commits sit between green and red. You want
the FIRST commit that broke things. Reading them is O(n). Bisecting
is O(log n). Same logic applies to any ordered sequence of changes.

You're given:
  - `start_state`: the initial value.
  - `changes`: a list of unary functions, each taking the current
    state and returning a new state.
  - `is_ok(state) -> bool`: invariant. True at start_state.

Find and return the index of the FIRST change after which `is_ok`
becomes False. Return None if every change is fine.

Constraint: call `is_ok` AT MOST O(log n) times in the worst case
(plus one initial call). The tests check this with a counter.
"""
from typing import Any, Callable


def bisect_failures(
    start_state: Any,
    changes: list[Callable[[Any], Any]],
    is_ok: Callable[[Any], bool],
) -> int | None:
    """Return the index of the first change that breaks `is_ok`.

    Implementation hint:
      - Pre-compute states[k] = state after applying changes[:k].
        states[0] is start_state. (This is O(n) state transitions —
        unavoidable since you can only apply changes in order.)
      - Then binary-search for the smallest k > 0 where is_ok fails.

    Why pre-compute? In a real `git bisect` you can checkout any
    commit, so the states are random-access. Same trick here.
    """
    # TODO: implement.
    raise NotImplementedError
