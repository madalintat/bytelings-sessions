"""Rung 3: Guided implement — fill in the Stack class.

Topic: a real stack class with push, pop, peek, len, and an empty-error.
"""


class Stack:
    """A LIFO stack backed by a Python list.

    Operations:
        push(x):  add x on top                      O(1) amortized
        pop():    remove and return top             O(1)
        peek():   return top without removing       O(1)
        len(s):   number of items                   O(1)
        bool(s):  False when empty, True otherwise  O(1)

    pop() and peek() must raise IndexError on an empty stack with the
    message "<op> from empty stack" so callers get a clear signal.

    >>> s = Stack()
    >>> s.push(1); s.push(2)
    >>> s.peek()
    2
    >>> len(s)
    2
    >>> s.pop()
    2
    """

    def __init__(self) -> None:
        # TODO: store items in a private list
        raise NotImplementedError

    def push(self, x) -> None:
        # TODO
        raise NotImplementedError

    def pop(self):
        # TODO: raise IndexError("pop from empty stack") when empty
        raise NotImplementedError

    def peek(self):
        # TODO: raise IndexError("peek from empty stack") when empty
        raise NotImplementedError

    def __len__(self) -> int:
        # TODO
        raise NotImplementedError

    def __bool__(self) -> bool:
        # Default __bool__ would call __len__ — leave this as-is.
        return len(self) > 0
