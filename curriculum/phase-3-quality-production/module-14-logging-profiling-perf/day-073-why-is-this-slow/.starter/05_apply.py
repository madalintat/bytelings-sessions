"""Rung 5: Apply.

Compare a naive O(n^2) implementation to the set-based one from rung 4.
Print the speedup. The point: same correctness, very different curve.

Try it: uv run python 05_apply.py
"""
import time
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location("_solo", Path(__file__).parent / "04_solo.py")
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def naive_find_pairs(xs: list[int], target: int) -> list[tuple[int, int]]:
    out: list[tuple[int, int]] = []
    seen: set[tuple[int, int]] = set()
    for i, a in enumerate(xs):
        for b in xs[i + 1:]:
            if a + b == target:
                pair = (a, b) if a < b else (b, a)
                if pair not in seen:
                    seen.add(pair)
                    out.append(pair)
    return sorted(out)


def time_it(fn, *args) -> float:
    start = time.perf_counter()
    fn(*args)
    return time.perf_counter() - start


def main() -> None:
    for n in (2_000, 5_000, 10_000):
        xs = list(range(n))
        target = n + n - 3  # only a few pairs
        t_naive = time_it(naive_find_pairs, xs, target)
        t_fast = time_it(_solo.find_pairs, xs, target)
        speedup = t_naive / max(t_fast, 1e-9)
        print(f"n={n:>6} naive={t_naive*1000:7.2f}ms fast={t_fast*1000:7.2f}ms speedup={speedup:6.1f}x")


if __name__ == "__main__":
    main()
