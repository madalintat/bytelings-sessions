"""Rung 3: Guided implement — solved version.

run_jobs wraps each callable in try/except. On success: log.info.
On exception: log.exception (auto-attaches the traceback). The
success count is returned so callers can react to partial failure.
"""
import logging
from typing import Callable

log = logging.getLogger(__name__)


def run_jobs(jobs: list[Callable[[], None]]) -> int:
    """Run each job. Return the number that succeeded."""
    successes = 0
    for job in jobs:
        try:
            job()
            log.info("job %s ok", job.__name__)
            successes += 1
        except Exception:
            log.exception("job %s failed", job.__name__)
    return successes
