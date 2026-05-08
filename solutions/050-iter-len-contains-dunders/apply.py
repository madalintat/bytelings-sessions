"""Rung 5: Apply — ducktype the container protocol onto an existing class.

Solo (rung 4) had you build OrderedSet from scratch with the dunders
baked in. That proves you can implement the container protocol. This
rung asks the harder, more realistic question: can you bolt the
container protocol onto a class you didn't write?

Here's a `RingBuffer`: a fixed-capacity FIFO that overwrites the
oldest item on overflow. Its internals are an `__init__`, a `.put()`,
and a `.dump()`. None of those let you write `len(rb)`, `for x in rb`,
or `x in rb` directly.

Your job: add `__len__`, `__iter__`, and `__contains__` so the asserts
in main() pass. Don't touch put/dump/__init__ — the discipline is
extending an existing API, not rewriting it.

Concept: the container protocol is how Python's generic operators
(`len`, `for`, `in`) reach into your domain model. Once you implement
the protocol, every standard-library iteration tool — `list(...)`,
`enumerate`, `*splat`, `tuple(...)` — works for free.

Run it:
    uv run python apply.py
"""
from collections import deque


class RingBuffer:
    """Fixed-size FIFO ring; overwrites the oldest item on overflow.

    Internals (provided): a deque with maxlen=capacity. You don't need
    to know how the deque works — just expose len/iter/contains via
    the dunders.
    """

    def __init__(self, capacity: int) -> None:
        self._capacity = capacity
        self._buffer: deque[object] = deque(maxlen=capacity)

    def put(self, item: object) -> None:
        self._buffer.append(item)

    def dump(self) -> list[object]:
        return list(self._buffer)

    # TODO: add __len__, __iter__, __contains__ here.
    # Hint: each one is a one-liner that delegates to self._buffer.


def main() -> None:
    rb = RingBuffer(capacity=3)
    for item in ("a", "b", "c", "d"):
        rb.put(item)
    # "a" was evicted by "d" — capacity is 3, FIFO order.

    assert len(rb) == 3, f"expected len=3, got {len(rb)}"
    assert list(rb) == ["b", "c", "d"], f"iteration wrong: {list(rb)}"
    assert "c" in rb, "'c' should still be in rb"
    assert "a" not in rb, "'a' was evicted, should not be in rb"

    # Free wins from the protocol (no extra dunders needed):
    assert tuple(rb) == ("b", "c", "d")
    assert sum(1 for _ in rb) == 3
    indexed = list(enumerate(rb))
    assert indexed == [(0, "b"), (1, "c"), (2, "d")]

    print("✓ Container protocol bolted onto RingBuffer.")
    print(f"  len = {len(rb)}, items = {list(rb)}, 'b' in rb = {'b' in rb}")


if __name__ == "__main__":
    main()
