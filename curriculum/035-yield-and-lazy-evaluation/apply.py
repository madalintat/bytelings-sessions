"""Rung 5: Apply — write a NEW lazy combinator (pairwise).

Solo gave you `naturals()` and `take_while`. Apply asks for a third
combinator that you build from scratch and then *compose with both*.

Implement `pairwise(iterable)`: a lazy generator that yields adjacent
pairs from `iterable`. Given (a, b, c, d) it yields (a, b), (b, c),
(c, d). For inputs of length < 2, yields nothing.

The crucial property: pairwise must be LAZY. It cannot pull all of
`iterable` into a list and then loop — you'll be running it on
solo's infinite `naturals()`. If you materialize the input,
`list(pairwise(naturals()))` will hang forever.

Concept (the day's NEW one): generators *compose*. Once you can write
one yield-based combinator, you can pipe an infinite source through a
chain of them and stop pulling whenever you've seen enough. That's
the property finite list-based code can't give you.

Run it:
    uv run python apply.py

Patterns: P-07 (accumulator-into-dict), P-12 (filter-then-map), P-16 (yield-from-passthrough), P-31 (string-build-via-list-then-join).
"""
from __future__ import annotations

from collections.abc import Iterable, Iterator
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location("_solo", Path(__file__).parent / "solo.py")
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


# TODO: implement pairwise() as a lazy generator.
# Hint: pull the iterator once with iter(), capture a "previous" value,
# then loop with `for current in it: yield (prev, current); prev = current`.
def pairwise(iterable: Iterable) -> Iterator[tuple]:
    raise NotImplementedError


def main() -> None:
    # Finite source — verify shape.
    finite = list(pairwise([1, 2, 3, 4]))
    assert finite == [(1, 2), (2, 3), (3, 4)], (
        f"pairwise([1,2,3,4]) should give [(1,2),(2,3),(3,4)], got {finite!r}."
    )

    # Single-element and empty — no pairs.
    assert list(pairwise([7])) == []
    assert list(pairwise([])) == []

    # Strings work — anything iterable.
    assert list(pairwise("abcd")) == [("a", "b"), ("b", "c"), ("c", "d")]

    # The big one: chained with solo's infinite naturals + take_while.
    # We pull just a few pairs from an infinite source — laziness or bust.
    nats = _solo.naturals()                              # 1, 2, 3, ... forever
    pairs = pairwise(nats)                               # (1,2), (2,3), (3,4), ...
    bounded = _solo.take_while(lambda p: p[0] < 5, pairs)  # stop when first elem >= 5
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
