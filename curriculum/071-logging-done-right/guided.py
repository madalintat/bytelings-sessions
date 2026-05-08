"""Rung 3: Guided implement — log.exception in an error handler.

Topic: capturing tracebacks in logs without losing them.

Real-world framing: a job runner that takes a list of callables,
runs each, and logs failures with full traceback. On success, it
logs at INFO. The runner returns a count of successes.
"""
import logging
from typing import Callable

log = logging.getLogger(__name__)


def run_jobs(jobs: list[Callable[[], None]]) -> int:
    """Run each job. Return the number that succeeded.

    Behavior:
      - For each job: call it.
        - If it succeeds, log at INFO with the message
          "job %s ok" and the job's __name__.
        - If it raises Exception, log at ERROR via `log.exception(...)`
          with the message "job %s failed" and the job's __name__.
          Then keep going (do NOT propagate).
      - Return the number of successes.

    Hints:
      - log.exception(...) auto-attaches the current traceback. Use
        it INSIDE the except block.
      - Use callable.__name__ for the job's name.
    """
    # TODO: implement.
    raise NotImplementedError
