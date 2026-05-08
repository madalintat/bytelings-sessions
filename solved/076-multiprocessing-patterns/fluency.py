"""Rung 2: Fluency drill — solved version.

Define _worker at module level (top-level picklable function) and
pass it to pool.map instead of the lambda. ProcessPoolExecutor
requires picklable workers; lambdas are not.

Two boilerplate hoops only the curriculum's dynamic loader forces:
  1. The loader names this module "_076-...-rung_2" — illegal Python
     identifier. We alias it under a legal name in sys.modules and
     override __name__ so functions defined below get a picklable
     __module__. (The test loader uses _byte.load_rung, which puts
     us in sys.modules under the original name; this alias adds the
     legal one alongside.)
  2. macOS Python defaults to "spawn", which re-imports each module
     by name — the hyphen-named original is unimportable, so spawn
     pickling fails. "fork" via mp_context inherits sys.modules
     (including the alias) instead of re-importing.

Real production code with normal module names doesn't need either.
"""
import multiprocessing
import sys
from concurrent.futures import ProcessPoolExecutor

_LEGAL_NAME = "_bytelings_d076_fluency"
sys.modules[_LEGAL_NAME] = sys.modules[__name__]
__name__ = _LEGAL_NAME


def _worker(x: int) -> int:
    return x * x + 1


def compute(items: list[int]) -> list[int]:
    ctx = multiprocessing.get_context("fork")
    with ProcessPoolExecutor(max_workers=2, mp_context=ctx) as pool:
        return list(pool.map(_worker, items))
