"""Rung 4: Solo implement.

Topic: structured logging — pass context as args, not in the message.

Implement `audit(action, **context)`:

  - Logs at INFO on the module-level logger named "audit".
  - Message template is exactly: "audit %s context=%s"
  - First arg: `action` (a string).
  - Second arg: a dict of the kwargs (so the formatted output
    interpolates the dict cleanly).

Reasoning: a log aggregator can pull the dict back out as JSON,
keeping fields searchable.

Hidden tests in 04_solo_test.py.

Patterns: P-01 (sentinel-loop), P-03 (walrus-in-condition).
"""
import logging

log = logging.getLogger("audit")


def audit(action: str, **context) -> None:
    raise NotImplementedError
