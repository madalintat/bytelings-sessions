"""Rung 4: Solo implement — solved version.

Map _square over items in a ProcessPoolExecutor, then sum the results
in the main process (reduce is cheap here). Empty list returns 0 via
sum of an empty iterable.
"""
from concurrent.futures import ProcessPoolExecutor


def _square(x: int) -> int:
    return x * x


def parallel_sum_of_squares(items: list[int], max_workers: int = 4) -> int:
    if not items:
        return 0
    with ProcessPoolExecutor(max_workers=max_workers) as pool:
        squares = pool.map(_square, items)
    return sum(squares)
