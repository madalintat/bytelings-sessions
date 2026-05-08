"""Rung 3: Guided — solved version.

sort_events uses a single tuple key (priority, time, user). Python's
stable Timsort guarantees that entries that compare equal on ALL three
fields preserve their original relative order. The tuple key composes
all three criteria into one pass, which is the simplest approach.

Alternatively: three stable sorts in reverse priority (user → time →
priority) also works and is shown as a comment.
"""


def sort_events(events: list[dict]) -> list[dict]:
    """Sort by priority asc, then time asc, then user asc."""
    return sorted(events, key=lambda e: (e["priority"], e["time"], e["user"]))
