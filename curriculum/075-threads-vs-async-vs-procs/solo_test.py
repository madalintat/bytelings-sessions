"""HIDDEN tests for rung 4 — do not peek before solving solo.py."""
import asyncio
import time
from pathlib import Path

from _byte import load_rung

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
ex = load_rung(_HERE / "solo.py", _NAME)


async def fast_fetcher(url: str) -> str:
    await asyncio.sleep(0.05)
    return url + "!"


def test_run_sync_basic():
    urls = ["a", "bb", "ccc"]
    out = ex.run_sync(urls, fast_fetcher)
    assert out == [2, 3, 4]


def test_run_sync_empty():
    assert ex.run_sync([], fast_fetcher) == []


def test_actually_concurrent():
    """5 fetchers of 50ms each should overlap — total < 0.2s."""
    urls = ["a", "b", "c", "d", "e"]
    start = time.perf_counter()
    ex.run_sync(urls, fast_fetcher)
    elapsed = time.perf_counter() - start
    assert elapsed < 0.2, f"not concurrent: {elapsed:.2f}s"


def test_async_function_is_coroutine():
    coro = ex.async_gather_lengths(["a"], fast_fetcher)
    # awaitable / coroutine
    assert asyncio.iscoroutine(coro)
    coro.close()
