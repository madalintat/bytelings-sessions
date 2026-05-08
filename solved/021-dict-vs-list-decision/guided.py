"""Rung 3: Guided — solved version.

`Roster` builds TWO dict indices from one list, so both `by_id` and
`by_email` are O(1) lookups:
  - `self._by_id = {c["id"]: c for c in contacts}`
  - `self._by_email = {c["email"]: c for c in contacts}`

`names_sorted` pulls names from the original list (or from .values())
and sorts them. Using the raw contacts list preserves memory-sharing
(no copies of the contact dicts).

This is the "list + dict indices" pattern: the list owns the data,
the dicts are lightweight lookup structures that point into the same objects.
"""


class Roster:
    """Holds a list of contacts with fast lookup by id AND by email."""

    def __init__(self, contacts: list[dict]) -> None:
        self._contacts = contacts
        self._by_id = {c["id"]: c for c in contacts}
        self._by_email = {c["email"]: c for c in contacts}

    def by_id(self, contact_id: int) -> dict | None:
        """O(1) lookup by id."""
        return self._by_id.get(contact_id)

    def by_email(self, email: str) -> dict | None:
        """O(1) lookup by email."""
        return self._by_email.get(email)

    def names_sorted(self) -> list[str]:
        """Return all names alphabetically."""
        return sorted(c["name"] for c in self._contacts)
