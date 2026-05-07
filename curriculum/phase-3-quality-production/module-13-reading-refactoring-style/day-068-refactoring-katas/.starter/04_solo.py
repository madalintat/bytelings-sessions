"""Rung 4: Solo implement.

Topic: a real refactor. Same interface, much cleaner internals.

Below is `format_user_label(user)` — a tangled function. The hidden
tests pin down its behavior. Refactor it freely. Constraints:

  - The PUBLIC name must remain `format_user_label`.
  - It must accept the same dict shape as input.
  - It must return the same strings the original returned.
  - You SHOULD extract at least one helper function.
  - You SHOULD remove the deeply nested ifs (target: max nesting depth 2).

The hidden tests will catch behavior regressions.
"""


def format_user_label(user: dict) -> str:
    if user is None:
        return "anonymous"
    if "name" in user and user["name"]:
        if "title" in user and user["title"]:
            if "suffix" in user and user["suffix"]:
                return f"{user['title']} {user['name']} {user['suffix']}"
            else:
                return f"{user['title']} {user['name']}"
        else:
            if "suffix" in user and user["suffix"]:
                return f"{user['name']} {user['suffix']}"
            else:
                return user["name"]
    else:
        if "email" in user and user["email"]:
            return user["email"]
        else:
            return "anonymous"
