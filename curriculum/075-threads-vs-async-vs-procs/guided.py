"""Rung 3: Guided implement — choose the right tool given a workload tag.

Topic: encoding the decision tree.

Real-world framing: a config-driven runner. The config says what the
work is — "io" or "cpu" — and the runner picks ThreadPool or
ProcessPool accordingly.

For learning, we keep the worker function trivial and use a flag,
but the decision logic is what matters.
"""
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from typing import Any, Callable


def run(
    workload: str,
    fn: Callable[[Any], Any],
    items: list[Any],
    max_workers: int = 4,
) -> list[Any]:
    """Run fn over items, choosing the executor by `workload`.

    Behavior:
      - workload == "io"  -> ThreadPoolExecutor (threads, GIL releases on I/O)
      - workload == "cpu" -> ProcessPoolExecutor (real parallelism)
      - any other value   -> raise ValueError("unknown workload: <x>")

    Returns the list of fn(item) results IN INPUT ORDER (use pool.map).
    """
    # TODO: implement the if/elif/else and call pool.map.
    raise NotImplementedError
