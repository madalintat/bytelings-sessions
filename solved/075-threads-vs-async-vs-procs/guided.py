"""Rung 3: Guided implement — solved version.

Pick ThreadPoolExecutor for "io" workloads and ProcessPoolExecutor for
"cpu" workloads. Raise ValueError for anything else. pool.map returns
results in input order.

The cpu branch uses mp_context="fork" so worker processes inherit the
caller's sys.modules — needed because the curriculum's dynamic loader
gives modules hyphenated names that macOS's default "spawn" can't
re-import. Real production code doesn't need this hint.
"""
import multiprocessing
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
        with ThreadPoolExecutor(max_workers=max_workers) as pool:
            return list(pool.map(fn, items))
    if workload == "cpu":
        ctx = multiprocessing.get_context("fork")
        with ProcessPoolExecutor(max_workers=max_workers, mp_context=ctx) as pool:
            return list(pool.map(fn, items))
    raise ValueError(f"unknown workload: {workload}")
