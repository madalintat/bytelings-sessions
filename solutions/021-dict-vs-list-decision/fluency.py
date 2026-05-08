"""Rung 2: Fluency drill — pick the right shape.

Topic: list vs dict
"""


def index_by_id(users: list[dict]) -> dict[int, dict]:
    """Return {user_id: user_dict} for the list of users.

    `users` is a list of dicts each with at least an 'id' key.
    Use a dict comprehension.
    """
    # TODO: this builds another list, not the index dict
    return [u["id"] for u in users]


def find_user(users_by_id: dict[int, dict], target: int) -> dict | None:
    """Return the user with this id, or None if not present.

    Must be O(1). No loops.
    """
    # TODO: don't loop — use dict.get
    for k, v in users_by_id.items():
        if k == target:
            return v
    return None


def names_sorted(users_by_id: dict[int, dict]) -> list[str]:
    """Return all user 'name' fields sorted alphabetically.

    Hint: dict.values() yields the user dicts; sorted accepts a key fn.
    """
    # TODO: sorts by id, not name
    return [users_by_id[k]["name"] for k in sorted(users_by_id)]
