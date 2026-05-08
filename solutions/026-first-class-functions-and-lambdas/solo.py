"""Rung 4: Solo implement.

Topic: a tiny pipeline runner over a list of (name, fn) steps

Implement `pipeline(steps)`:

- `steps` is a list of (str, callable) tuples — a name and a function.
- Returns a function `run(value)` that applies each step in order.
- `run(value)` returns a tuple (final_value, trace) where:
  - final_value is the value after all steps.
  - trace is a list of (step_name, value_after_step) tuples.
- An empty steps list: run(value) returns (value, []).

Example:
    steps = [
        ('plus_one', lambda x: x + 1),
        ('times_two', lambda x: x * 2),
        ('to_str', str),
    ]
    run = pipeline(steps)
    final, trace = run(3)
    # final == '8'
    # trace == [('plus_one', 4), ('times_two', 8), ('to_str', '8')]

The tests in 04_solo_test.py are HIDDEN. Don't peek before you try.

Patterns: P-17 (closure-over-counter).
"""
from typing import Callable


def pipeline(steps: list[tuple[str, Callable]]) -> Callable:
    raise NotImplementedError
