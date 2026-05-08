"""Rung 3: Guided implement — chunked map for small fast tasks.

Topic: chunksize tuning to amortize the per-task overhead.

Real-world framing: hashing a million short strings. With default
chunksize, the IPC overhead can dominate; passing chunksize=1000
batches them up.

Implement `parallel_hash(items, chunksize=1000)`:

  - Use ProcessPoolExecutor.
  - Use `pool.map(_hash_one, items, chunksize=chunksize)`.
  - Return the list of hex digests in input order.
"""
from concurrent.futures import ProcessPoolExecutor
import hashlib


def _hash_one(item: str) -> str:
    """Small, fast, CPU-bound — perfect for chunked mapping."""
    return hashlib.sha256(item.encode()).hexdigest()


def parallel_hash(items: list[str], chunksize: int = 1000) -> list[str]:
    """Hash each item in parallel and return digests in input order."""
    # TODO: implement using ProcessPoolExecutor and pool.map(_hash_one, ..., chunksize=chunksize).
    raise NotImplementedError
