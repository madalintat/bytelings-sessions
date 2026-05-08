"""Rung 2: Fluency drill — solved version.

Switch ThreadPoolExecutor to ProcessPoolExecutor for CPU-bound hashing.
The import line is updated too; _hash_one stays at module level so it
can be pickled across process boundaries.
"""
import hashlib
from concurrent.futures import ProcessPoolExecutor


def _hash_one(item: str) -> str:
    h = hashlib.sha256()
    for _ in range(50):
        h.update(item.encode())
    return h.hexdigest()


def hash_many(items: list[str]) -> list[str]:
    with ProcessPoolExecutor() as pool:
        return list(pool.map(_hash_one, items))
