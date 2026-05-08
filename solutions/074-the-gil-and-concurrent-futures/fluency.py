"""Rung 2: Fluency drill — parallelize an I/O-bound loop with threads.

Topic: ThreadPoolExecutor.map.

`fake_fetch(url)` simulates a network call by sleeping 100 ms then
returning a fake status. The sequential `fetch_all` runs 10 of them
serially — about 1 second total. With a ThreadPoolExecutor it should
finish in well under 0.5 seconds (the 10 sleeps overlap).

Rewrite `fetch_all` to use ThreadPoolExecutor.map.
"""
import time


def fake_fetch(url: str) -> int:
    time.sleep(0.1)  # simulated I/O wait
    return len(url)


def fetch_all(urls: list[str]) -> list[int]:
    # TODO: replace this sequential loop with a ThreadPoolExecutor
    # using max_workers=8 and pool.map(fake_fetch, urls).
    return [fake_fetch(u) for u in urls]
