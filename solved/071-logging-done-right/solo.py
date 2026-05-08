"""Rung 4: Solo implement — solved version.

audit() logs at INFO on the "audit" logger. The message template uses
%s so the dict stays as a structured second argument — log aggregators
can separate template from data.
"""
import logging

log = logging.getLogger("audit")


def audit(action: str, **context) -> None:
    log.info("audit %s context=%s", action, context)
