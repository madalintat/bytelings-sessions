"""Rung 2: Fluency drill — solved version.

Replace each print() with the appropriate log level using %s form
(not f-strings), so log filtering skips string formatting when the
level is suppressed.
"""
import logging

log = logging.getLogger(__name__)


def process(user_id: str, payload: dict) -> dict | None:
    log.info("start processing user_id=%s", user_id)
    if not payload:
        log.warning("empty payload for user_id=%s", user_id)
        return None
    if "fatal" in payload:
        log.error("fatal flag set for user_id=%s", user_id)
        return None
    log.info("done processing user_id=%s", user_id)
    return {"ok": True}
