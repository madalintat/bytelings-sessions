"""Rung 2: Fluency drill — switch threads to processes for CPU work.

Topic: pick the right pool.

`hash_many(items)` runs a CPU-bound hash over each item. Threads
don't help here (GIL). Switch ThreadPoolExecutor to ProcessPoolExecutor.

Note: ProcessPoolExecutor needs the worker function to be importable
(no lambdas / locals). `_hash_one` at module level fits the bill.
"""
import hashlib
from concurrent.futures import ThreadPoolExecutor


def _hash_one(item: str) -> str:
    h = hashlib.sha256()
    # do enough work that parallelism would matter
    for _ in range(50):
        h.update(item.encode())
    return h.hexdigest()


def hash_many(items: list[str]) -> list[str]:
    # TODO: change ThreadPoolExecutor to ProcessPoolExecutor.
    # (Update the import above too.)
    with ThreadPoolExecutor() as pool:
        return list(pool.map(_hash_one, items))
