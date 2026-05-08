"""Rung 2: Fluency drill — solved version.

Switch ThreadPoolExecutor to ProcessPoolExecutor for CPU-bound hashing.
_hash_one stays at module level so it can be pickled across process
boundaries.

Two boilerplate hoops the curriculum's dynamic loader forces here:
  1. The loader names this module "_075-...-rung_2" — illegal Python
     identifier (hyphens), unimportable by name. We alias it under a
     legal name in sys.modules and override __name__ so functions
     defined below get a picklable __module__.
  2. macOS Python defaults to "spawn" workers, which re-import each
     module by name; with our hyphen-named original, that fails. We
     pin the start method to "fork" via mp_context, which inherits the
     parent's sys.modules (including our alias) instead of re-importing.

Real production code with files named like normal modules doesn't need
either hoop.
"""
import hashlib
import multiprocessing
import sys
from concurrent.futures import ProcessPoolExecutor

_LEGAL_NAME = "_bytelings_d075_fluency"
sys.modules[_LEGAL_NAME] = sys.modules[__name__]
__name__ = _LEGAL_NAME


def _hash_one(item: str) -> str:
    h = hashlib.sha256()
    for _ in range(50):
        h.update(item.encode())
    return h.hexdigest()


def hash_many(items: list[str]) -> list[str]:
    ctx = multiprocessing.get_context("fork")
    with ProcessPoolExecutor(mp_context=ctx) as pool:
        return list(pool.map(_hash_one, items))
