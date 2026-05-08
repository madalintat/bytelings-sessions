"""Rung 2: Fluency — solved version.

sort_by_name_then_age: the tuple key is (age, name) but should be
  (name, age) — primary sort by name, tiebreak by age.

sort_descending_age_then_name: to sort age descending while name
  stays ascending, negate the age component: key=(-age, name).
"""


def sort_by_name_then_age(people: list[tuple[str, int]]) -> list[tuple[str, int]]:
    """Sort by name ascending, age ascending as tiebreaker."""
    return sorted(people, key=lambda p: (p[0], p[1]))


def sort_descending_age_then_name(people: list[tuple[str, int]]) -> list[tuple[str, int]]:
    """Sort by age descending, name ascending as tiebreaker."""
    return sorted(people, key=lambda p: (-p[1], p[0]))
