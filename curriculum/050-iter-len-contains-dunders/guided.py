"""Rung 3: Guided implement.

Topic: __getitem__ + __len__

Build `Deck`, a small ordered collection of strings:
- __init__(self, cards: list[str]) stores a copy.
- __len__(self) returns the count.
- __getitem__(self, index) returns the card at that index.
- A `shuffle(self, rng)` method that takes a random.Random instance
  and shuffles in place using rng.shuffle.

Iteration should fall out for free when __len__ + __getitem__ are
defined — the legacy iteration protocol uses these.
"""


class Deck:
    def __init__(self, cards: list[str]) -> None:
        # TODO: store a copy
        raise NotImplementedError

    # TODO: __len__
    # TODO: __getitem__

    def shuffle(self, rng) -> None:
        # TODO: rng.shuffle(self._cards)
        raise NotImplementedError
