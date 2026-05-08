"""Rung 5: Apply.

Tiny CLI: simulate a flaky operation N times (argv) using the retry
decorator and print success/failure counts.

Reuses retry from rung 4.

Try it: uv run python apply.py 5
"""
import random
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location(
    "_solo", Path(__file__).parent / "solo.py"
)
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


@_solo.retry
def flaky() -> str:
    if random.random() < 0.4:
        raise RuntimeError("transient")
    return "ok"


def main() -> None:
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    random.seed(42)
    results = []
    for _ in range(n):
        try:
            results.append(flaky())
        except RuntimeError:
            results.append("FAILED")
    print(f"results: {results}")
    print(f"successes={flaky.successes}, failures={flaky.failures}")


if __name__ == "__main__":
    main()
