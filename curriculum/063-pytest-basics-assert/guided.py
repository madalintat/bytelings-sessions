"""Rung 3: Guided implement — `Counter` + tests for it.

Topic: writing the unit AND its tests, hitting common-case + edges.

Real-world framing: you're writing a tiny request counter for a rate
limiter. It increments per key and resets on demand.

The class is partially built. Fill in the methods. Tests live next door
and will tell you if your behavior matches the contract.
"""


class Counter:
    """Per-key request counter."""

    def __init__(self) -> None:
        # TODO: a dict[str, int]
        raise NotImplementedError

    def hit(self, key: str) -> int:
        """Increment count for `key` and return the new value."""
        # TODO
        raise NotImplementedError

    def value(self, key: str) -> int:
        """Return current count for `key`, or 0 if unseen."""
        # TODO
        raise NotImplementedError

    def reset(self, key: str) -> None:
        """Reset count for `key` to 0. No-op if unseen."""
        # TODO
        raise NotImplementedError
