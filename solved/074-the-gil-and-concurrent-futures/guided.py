"""Rung 3: Guided implement — solved version.

Submit all URLs, collect results with as_completed. Catch any exception
from future.result() and format it as "error: <message>" so one
failure never breaks the rest.
"""
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Callable


def gather_results(
    urls: list[str],
    fetch: Callable[[str], str],
    max_workers: int = 8,
) -> dict[str, str]:
    """Run fetch(url) for each URL in a thread pool."""
    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        futures = {pool.submit(fetch, url): url for url in urls}
        results: dict[str, str] = {}
        for fut in as_completed(futures):
            url = futures[fut]
            try:
                results[url] = fut.result()
            except Exception as e:
                results[url] = f"error: {e}"
    return results
