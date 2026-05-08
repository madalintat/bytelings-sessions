"""Rung 4: Solo implement — solved version.

Use pool.map which preserves input order. Catch exceptions per-future
by submitting individually with submit() + a result list that stores
Exception objects on failure.
"""
from concurrent.futures import ThreadPoolExecutor
from typing import Any, Callable


def parallel_apply(
    items: list[Any],
    fn: Callable[[Any], Any],
    max_workers: int = 8,
) -> list[Any]:
    """Apply fn to each item in parallel, returning results in input order.
    On exception, the corresponding slot holds the Exception object."""
    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        futures = [pool.submit(fn, item) for item in items]
    results = []
    for fut in futures:
        try:
            results.append(fut.result())
        except Exception as e:
            results.append(e)
    return results
