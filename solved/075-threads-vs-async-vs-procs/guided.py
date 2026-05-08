"""Rung 3: Guided implement — solved version.

Pick ThreadPoolExecutor for "io" workloads and ProcessPoolExecutor for
"cpu" workloads. Raise ValueError for anything else. pool.map returns
results in input order.
"""
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from typing import Any, Callable


def run(
    workload: str,
    fn: Callable[[Any], Any],
    items: list[Any],
    max_workers: int = 4,
) -> list[Any]:
    """Run fn over items, choosing the executor by `workload`."""
    if workload == "io":
        executor_cls = ThreadPoolExecutor
    elif workload == "cpu":
        executor_cls = ProcessPoolExecutor
    else:
        raise ValueError(f"unknown workload: {workload}")

    with executor_cls(max_workers=max_workers) as pool:
        return list(pool.map(fn, items))
