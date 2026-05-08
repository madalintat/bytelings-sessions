"""Rung 2: Fluency — solved version.

Three dict-vs-list decision exercises:
  1. index_by_id: the starter returns `[u["id"] for u in users]` — a list
     of IDs, not a dict. The correct shape is a dict comprehension:
     `{u["id"]: u for u in users}`.
  2. find_user: the loop defeats the O(1) benefit of a dict. Use
     `users_by_id.get(target)`, which is O(1).
  3. names_sorted: `sorted(users_by_id)` sorts by KEY (id, an int).
     The spec wants names sorted ALPHABETICALLY. Extract `.values()`,
     pull the 'name' field, and sort those.
"""


def index_by_id(users: list[dict]) -> dict[int, dict]:
    """Return {user_id: user_dict} for the list of users."""
    return {u["id"]: u for u in users}


def find_user(users_by_id: dict[int, dict], target: int) -> dict | None:
    """Return the user with this id, or None if not present. O(1)."""
    return users_by_id.get(target)


def names_sorted(users_by_id: dict[int, dict]) -> list[str]:
    """Return all user 'name' fields sorted alphabetically."""
    return sorted(u["name"] for u in users_by_id.values())
