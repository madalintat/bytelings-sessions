"""Rung 5: Apply.

A "safer driver" — runs a sequence of functions, prints a one-line
summary per failure using last_frame_summary from rung 4. Useful in
batch jobs where you want to log every error but keep going.

Try it: uv run python 05_apply.py
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location("_solo", Path(__file__).parent / "04_solo.py")
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def step_a():
    return "A ok"


def step_b():
    return int("not a number")


def step_c():
    return [1, 2, 3][99]


def main() -> None:
    steps = [step_a, step_b, step_c]
    for step in steps:
        result = _solo.last_frame_summary(step)
        if result is None:
            print(f"{step.__name__}: ok")
        else:
            print(f"{step.__name__}: FAIL - {result}")


if __name__ == "__main__":
    main()
