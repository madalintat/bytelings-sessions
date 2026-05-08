"""Rung 3: Guided — solved version.

`Deck` stores a copy of the card list so external modifications to the
original don't affect it. With `__len__` and `__getitem__` defined,
Python's legacy iteration protocol (getitem-based) works automatically
— no `__iter__` is needed, though adding one explicitly is fine.
`shuffle` mutates `self._cards` in place using the caller-supplied RNG.
"""


class Deck:
    def __init__(self, cards: list[str]) -> None:
        self._cards = list(cards)

    def __len__(self) -> int:
        return len(self._cards)

    def __getitem__(self, index: int) -> str:
        return self._cards[index]

    def shuffle(self, rng) -> None:
        rng.shuffle(self._cards)
