"""Rung 5: Apply.

Demonstrate the difference: same problem, three solutions, three
shapes of code.

Try it: uv run python 05_apply.py
"""
import asyncio
import time
from concurrent.futures import ThreadPoolExecutor


def io_fetch(url: str) -> str:
    time.sleep(0.05)  # simulated network
    return url + "!"


async def async_fetch(url: str) -> str:
    await asyncio.sleep(0.05)
    return url + "!"


URLS = [f"u{i}" for i in range(20)]


def time_it(label: str, fn) -> None:
    start = time.perf_counter()
    fn()
    print(f"{label:>10}: {(time.perf_counter() - start) * 1000:6.0f} ms")


def run_serial() -> None:
    [io_fetch(u) for u in URLS]


def run_threads() -> None:
    with ThreadPoolExecutor(max_workers=10) as pool:
        list(pool.map(io_fetch, URLS))


def run_async() -> None:
    async def main():
        return await asyncio.gather(*(async_fetch(u) for u in URLS))

    asyncio.run(main())


def main() -> None:
    print(f"20 fake fetches, 50ms each (so ~1s sequential).")
    time_it("serial", run_serial)
    time_it("threads", run_threads)
    time_it("async", run_async)


if __name__ == "__main__":
    main()
