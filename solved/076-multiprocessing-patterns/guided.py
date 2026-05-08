"""Rung 3: Guided implement — solved version.

parallel_hash uses ProcessPoolExecutor.map with the given chunksize to
batch small items and amortize IPC overhead. Results come back in input
order because pool.map preserves order.

The module-alias + fork-context dance below is curriculum boilerplate
(see fluency.py for the full explanation). Real production code with
normal module names doesn't need it.
"""
import hashlib
import multiprocessing
import sys
from concurrent.futures import ProcessPoolExecutor

_LEGAL_NAME = "_bytelings_d076_guided"
sys.modules[_LEGAL_NAME] = sys.modules[__name__]
__name__ = _LEGAL_NAME


def _hash_one(item: str) -> str:
    """Small, fast, CPU-bound — perfect for chunked mapping."""
    return hashlib.sha256(item.encode()).hexdigest()


def parallel_hash(items: list[str], chunksize: int = 1000) -> list[str]:
    """Hash each item in parallel and return digests in input order."""
    ctx = multiprocessing.get_context("fork")
    with ProcessPoolExecutor(mp_context=ctx) as pool:
        return list(pool.map(_hash_one, items, chunksize=chunksize))
