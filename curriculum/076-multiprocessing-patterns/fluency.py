"""Rung 2: Fluency drill — make the worker pickleable.

Topic: ProcessPoolExecutor's pickle requirement.

The `compute` function below uses a lambda, which can't be pickled
across processes. Define a top-level `_worker` function (above
`compute`), then pass `_worker` to pool.map.
"""
from concurrent.futures import ProcessPoolExecutor


# TODO: define `_worker(x: int) -> int` returning x * x + 1.


def compute(items: list[int]) -> list[int]:
    with ProcessPoolExecutor(max_workers=2) as pool:
        # TODO: replace the lambda with `_worker` (a top-level function).
        return list(pool.map(lambda x: x * x + 1, items))
