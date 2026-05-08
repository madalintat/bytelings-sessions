"""Rung 5: Apply — implement two variants of the SAME operation.

Solo (rung 4) had you write `dedupe` as a pure function (returns a
new list). That proved you could do one shape. This rung asks the
question every real codebase asks sooner or later: when do you
mutate, when do you return?

Write two functions that strip None values from a list:

    compact(lst) -> None        # in-place: mutates lst, returns None
    without_nones(lst) -> list  # pure: returns a new list, lst untouched

Both should keep non-None elements in their original order. The
asserts below verify the contract for each.

Concept (the day's NEW one — Pattern P-02 from `bytelings patterns`):
list.sort() vs sorted(), list.reverse() vs reversed() — Python uses
*naming* as the marker for which contract a function follows. Verbs
mutate; gerunds and `without_X` return. When you ship two helpers
that do the same logical thing, the naming makes the contract
discoverable.

Run it:
    uv run python apply.py
"""
from __future__ import annotations


# TODO: implement compact() — mutate `lst` in place, return None.
# Hint: `lst[:] = (x for x in lst if x is not None)` rebinds the
# slice in place without replacing the list object.
def compact(lst: list) -> None:
    raise NotImplementedError


# TODO: implement without_nones() — return a NEW list, leave `lst` untouched.
def without_nones(lst: list) -> list:
    raise NotImplementedError


def main() -> None:
    # ---- compact: in-place, returns None ----
    src = [1, None, 2, None, 3]
    result = compact(src)
    assert result is None, (
        f"compact should return None (in-place mutation), got {result!r}. "
        "Look at how list.sort() returns None — same shape."
    )
    assert src == [1, 2, 3], (
        f"compact should mutate src to [1, 2, 3], got {src!r}. "
        "Hint: lst[:] = (x for x in lst if x is not None) rebinds in place."
    )

    # ---- without_nones: pure, returns new list ----
    src2 = [1, None, 2, None, 3]
    snapshot = src2.copy()
    fresh = without_nones(src2)
    assert fresh == [1, 2, 3], (
        f"without_nones should return [1, 2, 3], got {fresh!r}."
    )
    assert src2 == snapshot, (
        f"without_nones must NOT mutate input. Before: {snapshot}, after: {src2}. "
        "Use a comprehension or generator that builds a new list."
    )
    assert fresh is not src2, (
        "without_nones must return a NEW list, not the same object."
    )

    # Edge: empty input.
    empty: list = []
    compact(empty)
    assert empty == []
    assert without_nones([]) == []

    print("✓ Both contracts honored.")
    print("  compact: in-place, returns None")
    print("  without_nones: pure, returns new list")


if __name__ == "__main__":
    main()
