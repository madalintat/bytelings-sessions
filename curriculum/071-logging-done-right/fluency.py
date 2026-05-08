"""Rung 2: Fluency drill — convert prints to a logger.

Topic: replacing print() with logging.

Steps:
  1. Replace each `print(...)` with the appropriate `log.<level>(...)`
     call (info / warning / error). The comments suggest which.
  2. Use the %s form, NOT f-strings.
"""
import logging

log = logging.getLogger(__name__)


def process(user_id: str, payload: dict) -> dict | None:
    print(f"start processing user_id={user_id}")  # TODO: log.info, %s form
    if not payload:
        print(f"empty payload for user_id={user_id}")  # TODO: log.warning
        return None
    if "fatal" in payload:
        print(f"fatal flag set for user_id={user_id}")  # TODO: log.error
        return None
    print(f"done processing user_id={user_id}")  # TODO: log.info
    return {"ok": True}
