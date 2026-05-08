"""Rung 3: Guided implement — solved version.

parallel_hash uses ProcessPoolExecutor.map with the given chunksize to
batch small items and amortize IPC overhead. Results come back in input
order because pool.map preserves order.
"""
from concurrent.futures import ProcessPoolExecutor
import hashlib


def _hash_one(item: str) -> str:
    """Small, fast, CPU-bound — perfect for chunked mapping."""
    return hashlib.sha256(item.encode()).hexdigest()


def parallel_hash(items: list[str], chunksize: int = 1000) -> list[str]:
    """Hash each item in parallel and return digests in input order."""
    with ProcessPoolExecutor() as pool:
        return list(pool.map(_hash_one, items, chunksize=chunksize))
