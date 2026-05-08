"""Rung 3: Guided implement — submit + as_completed with error handling.

Topic: streaming results as they finish, tolerating partial failure.

Real-world framing: you're checking the health of N services. Some
will time out, some will succeed. You want a dict mapping each url
to either its result or "error: <message>". Don't let one failure
break the rest.
"""
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Callable


def gather_results(
    urls: list[str],
    fetch: Callable[[str], str],
    max_workers: int = 8,
) -> dict[str, str]:
    """Run fetch(url) for each URL in a thread pool. Return:

      { url: result_string,            # on success
        url: f"error: {exception}" }   # on failure

    Implementation:
      - Use ThreadPoolExecutor with `max_workers`.
      - Submit each URL with pool.submit, build a dict {future: url}.
      - Iterate as_completed(futures).
      - For each future, try future.result(). On Exception, format
        the error string. Do NOT let it propagate.
    """
    # TODO: implement.
    raise NotImplementedError
