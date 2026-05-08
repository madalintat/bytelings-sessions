"""Rung 4: Solo implement — solved version.

Extract _display_name() to flatten the nested conditionals. The
helper builds the name from whichever parts are present; the outer
function handles the None and fallback-to-email cases.
"""


def _display_name(user: dict) -> str | None:
    """Build a display name from title, name, suffix. Returns None if no name."""
    name = user.get("name", "")
    if not name:
        return None
    parts = []
    if user.get("title"):
        parts.append(user["title"])
    parts.append(name)
    if user.get("suffix"):
        parts.append(user["suffix"])
    return " ".join(parts)


def format_user_label(user: dict) -> str:
    if user is None:
        return "anonymous"
    display = _display_name(user)
    if display:
        return display
    email = user.get("email", "")
    if email:
        return email
    return "anonymous"
