"""Rung 3: Guided implement — solved version.

Stack wraps a list. push/pop use append/pop() at the right end (O(1)).
peek returns the last element. Empty-operation errors use clear messages.
__bool__ delegates to __len__ via the default provided in the starter.
"""


class Stack:
    """A LIFO stack backed by a Python list."""

    def __init__(self) -> None:
        self._data: list = []

    def push(self, x) -> None:
        self._data.append(x)

    def pop(self):
        if not self._data:
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self):
        if not self._data:
            raise IndexError("peek from empty stack")
        return self._data[-1]

    def __len__(self) -> int:
        return len(self._data)

    def __bool__(self) -> bool:
        return len(self) > 0
