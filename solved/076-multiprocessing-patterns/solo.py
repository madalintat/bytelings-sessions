"""Rung 4: Solo implement — solved version.

Map _square over items in a ProcessPoolExecutor, then sum the results
in the main process (reduce is cheap here). Empty list returns 0 via
sum of an empty iterable.

The module-alias + fork-context dance below is curriculum boilerplate
(see fluency.py for the full explanation). Real production code with
normal module names doesn't need it.
"""
import multiprocessing
import sys
from concurrent.futures import ProcessPoolExecutor

_LEGAL_NAME = "_bytelings_d076_solo"
sys.modules[_LEGAL_NAME] = sys.modules[__name__]
__name__ = _LEGAL_NAME


def _square(x: int) -> int:
    return x * x


def parallel_sum_of_squares(items: list[int], max_workers: int = 4) -> int:
    if not items:
        return 0
    ctx = multiprocessing.get_context("fork")
    with ProcessPoolExecutor(max_workers=max_workers, mp_context=ctx) as pool:
        squares = pool.map(_square, items)
    return sum(squares)
