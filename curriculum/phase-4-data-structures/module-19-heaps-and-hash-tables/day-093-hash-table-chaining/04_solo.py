"""Rung 4: Solo implement.

Topic: write `HashSet` — a set with chaining, set semantics.

Operations:
    add(x)             - add x; no-op if already present
    remove(x)          - remove x; raise KeyError if not present
    discard(x)         - remove x; no-op if not present
    __contains__(x)    - bool
    __len__()
    __iter__()         - yields elements in any order

You may build it from scratch (don't import the rung-3 HashMap), or
internally back it with a dict-like — either is fine. The hidden
tests don't check internals, only behavior. The point is to feel
the same chaining shape twice and notice "set is map without values."

Examples:
    s = HashSet()
    s.add("a"); s.add("b"); s.add("a")
    assert "a" in s
    assert len(s) == 2

The tests in 04_solo_test.py are HIDDEN. Don't peek before you try.
"""


class HashSet:
    def __init__(self) -> None:
        raise NotImplementedError

    def add(self, x) -> None:
        raise NotImplementedError

    def remove(self, x) -> None:
        raise NotImplementedError

    def discard(self, x) -> None:
        raise NotImplementedError

    def __contains__(self, x) -> bool:
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError

    def __iter__(self):
        raise NotImplementedError
