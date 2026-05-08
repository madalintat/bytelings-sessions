"""Rung 5: Apply — solved version.

`pairwise` keeps a single "previous" value in scope. It calls `iter()`
once to get a plain iterator, reads the first item, then loops. At
each step it yields `(prev, current)` and advances `prev`. This is
O(1) memory regardless of source length — no buffering, no
materialisation. The compose test at the bottom confirms it works
lazily over an infinite `naturals()` source.
"""
from __future__ import annotations

from collections.abc import Iterable, Iterator
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location("_solo", Path(__file__).parent / "solo.py")
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def pairwise(iterable: Iterable) -> Iterator[tuple]:
    it = iter(iterable)
    try:
        prev = next(it)
    except StopIteration:
        return
    for current in it:
        yield (prev, current)
        prev = current


def main() -> None:
    finite = list(pairwise([1, 2, 3, 4]))
    assert finite == [(1, 2), (2, 3), (3, 4)], (
        f"pairwise([1,2,3,4]) should give [(1,2),(2,3),(3,4)], got {finite!r}."
    )

    assert list(pairwise([7])) == []
    assert list(pairwise([])) == []
    assert list(pairwise("abcd")) == [("a", "b"), ("b", "c"), ("c", "d")]

    nats = _solo.naturals()
    pairs = pairwise(nats)
    bounded = _solo.take_while(lambda p: p[0] < 5, pairs)
    materialized = list(bounded)
    assert materialized == [(1, 2), (2, 3), (3, 4), (4, 5)], (
        f"Pipeline (naturals → pairwise → take_while < 5) wrong: {materialized!r}. "
        "If this hangs, your pairwise is materializing the input — make it lazy."
    )

    print("✓ pairwise composes with naturals + take_while.")
    print(f"  finite([1,2,3,4]): {finite}")
    print(f"  infinite (first <5): {materialized}")


if __name__ == "__main__":
    main()
