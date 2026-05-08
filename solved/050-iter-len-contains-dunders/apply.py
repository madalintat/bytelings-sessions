"""Rung 5: Apply — solved version.

The three dunders (`__len__`, `__iter__`, `__contains__`) are added to
the provided `RingBuffer` class. Each is a one-liner that delegates to
the underlying `deque`, which already implements the container protocol.
"""
from collections import deque


class RingBuffer:
    """Fixed-size FIFO ring; overwrites the oldest item on overflow."""

    def __init__(self, capacity: int) -> None:
        self._capacity = capacity
        self._buffer: deque[object] = deque(maxlen=capacity)

    def put(self, item: object) -> None:
        self._buffer.append(item)

    def dump(self) -> list[object]:
        return list(self._buffer)

    def __len__(self) -> int:
        return len(self._buffer)

    def __iter__(self):
        return iter(self._buffer)

    def __contains__(self, item) -> bool:
        return item in self._buffer


def main() -> None:
    rb = RingBuffer(capacity=3)
    for item in ("a", "b", "c", "d"):
        rb.put(item)

    assert len(rb) == 3, f"expected len=3, got {len(rb)}"
    assert list(rb) == ["b", "c", "d"], f"iteration wrong: {list(rb)}"
    assert "c" in rb, "'c' should still be in rb"
    assert "a" not in rb, "'a' was evicted, should not be in rb"

    assert tuple(rb) == ("b", "c", "d")
    assert sum(1 for _ in rb) == 3
    indexed = list(enumerate(rb))
    assert indexed == [(0, "b"), (1, "c"), (2, "d")]

    print("✓ Container protocol bolted onto RingBuffer.")
    print(f"  len = {len(rb)}, items = {list(rb)}, 'b' in rb = {'b' in rb}")


if __name__ == "__main__":
    main()
