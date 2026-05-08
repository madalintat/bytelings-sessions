"""Rung 2: Fluency drill — fix the key functions.

Topic: stable sort + key= + tuples for multi-criteria sort.

`sort_by_name_then_age` should sort by name ascending, with age as a
tiebreaker (also ascending). It's currently sorting by age first
because the tuple is in the wrong order.

`sort_descending_age_then_name` should sort by age DESCENDING (oldest
first), then name ascending as a tiebreaker. It's currently sorting
ascending by age.

Each list contains (name, age) tuples.
"""


def sort_by_name_then_age(people: list[tuple[str, int]]) -> list[tuple[str, int]]:
    # TODO: tuple is backwards
    return sorted(people, key=lambda p: (p[1], p[0]))


def sort_descending_age_then_name(people: list[tuple[str, int]]) -> list[tuple[str, int]]:
    # TODO: age is ascending. Negate it (or use reverse= cleverly) so
    # age sorts descending while name still sorts ascending.
    return sorted(people, key=lambda p: (p[1], p[0]))
