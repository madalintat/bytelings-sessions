"""Rung 5: Apply.

Show insertion sort's best-case vs worst-case empirically — same
algorithm, very different comparison counts.

Try it: uv run python apply.py

Patterns: P-29 (binary-search-on-answer).
"""
import random
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location(
    "_solo", Path(__file__).parent / "solo.py"
)
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def main() -> None:
    n = 50
    sorted_arr = list(range(n))
    reverse_arr = list(range(n, 0, -1))
    random.seed(0)
    random_arr = random.sample(range(n), n)

    cases = [
        ("already sorted", sorted_arr),
        ("reverse sorted", reverse_arr),
        ("random       ", random_arr),
    ]
    for label, arr in cases:
        _, cmps = _solo.insertion_sort_with_stats(arr)
        print(f"{label}: {cmps} comparisons")


if __name__ == "__main__":
    main()
