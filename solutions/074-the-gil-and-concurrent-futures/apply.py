"""Rung 5: Apply.

Use parallel_apply to "fetch" the lengths of N fake URLs concurrently
and report total wall time.

Try it: uv run python apply.py
"""
import time
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location("_solo", Path(__file__).parent / "solo.py")
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def fake_fetch(url: str) -> int:
    time.sleep(0.05)  # simulated I/O
    return len(url)


def main() -> None:
    urls = [f"https://example.com/{i:03d}" for i in range(20)]
    start = time.perf_counter()
    results = _solo.parallel_apply(urls, fake_fetch, max_workers=10)
    elapsed = time.perf_counter() - start
    print(f"fetched {len(results)} URLs in {elapsed*1000:.0f}ms")
    print(f"first 3: {results[:3]}")


if __name__ == "__main__":
    main()
