"""Rung 3: Guided implement.

Topic: build TWO indices from one list, then answer queries

Implement `Roster` — a thin wrapper around a list of contact dicts
that supports fast lookup by id AND by email.
"""


class Roster:
    """Holds a list of contacts, plus two dict indices for fast lookup.

    Each contact is a dict with keys 'id' (int), 'email' (str), and
    'name' (str). Email is unique. Id is unique.

    >>> r = Roster([
    ...     {'id': 1, 'email': 'a@x.io', 'name': 'Alice'},
    ...     {'id': 2, 'email': 'b@x.io', 'name': 'Bob'},
    ... ])
    >>> r.by_id(1)['name']
    'Alice'
    >>> r.by_email('b@x.io')['name']
    'Bob'
    >>> r.by_id(99) is None
    True
    >>> r.names_sorted()
    ['Alice', 'Bob']
    """

    def __init__(self, contacts: list[dict]) -> None:
        # TODO: store contacts; build self._by_id and self._by_email
        # using dict comprehensions.
        raise NotImplementedError

    def by_id(self, contact_id: int) -> dict | None:
        """O(1) lookup by id."""
        # TODO
        raise NotImplementedError

    def by_email(self, email: str) -> dict | None:
        """O(1) lookup by email."""
        # TODO
        raise NotImplementedError

    def names_sorted(self) -> list[str]:
        """Return all names alphabetically."""
        # TODO
        raise NotImplementedError
