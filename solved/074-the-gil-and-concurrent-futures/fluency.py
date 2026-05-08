"""Rung 2: Fluency drill — solved version.

Replace the sequential list comprehension with ThreadPoolExecutor.map.
Ten 100ms sleeps that overlap take ~100ms total instead of ~1s.
"""
import time
from concurrent.futures import ThreadPoolExecutor


def fake_fetch(url: str) -> int:
    time.sleep(0.1)  # simulated I/O wait
    return len(url)


def fetch_all(urls: list[str]) -> list[int]:
    with ThreadPoolExecutor(max_workers=8) as pool:
        return list(pool.map(fake_fetch, urls))
