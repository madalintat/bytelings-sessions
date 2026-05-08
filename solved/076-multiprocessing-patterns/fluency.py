"""Rung 2: Fluency drill — solved version.

Define _worker at module level (top-level picklable function) and
pass it to pool.map instead of the lambda. ProcessPoolExecutor
requires picklable workers; lambdas are not.
"""
from concurrent.futures import ProcessPoolExecutor


def _worker(x: int) -> int:
    return x * x + 1


def compute(items: list[int]) -> list[int]:
    with ProcessPoolExecutor(max_workers=2) as pool:
        return list(pool.map(_worker, items))
