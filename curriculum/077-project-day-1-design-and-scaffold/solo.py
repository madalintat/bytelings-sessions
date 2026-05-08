"""Rung 4: Solo — synthetic log fixture.

Topic: building a deterministic fixture so tests don't need real log files.

Implement `make_log_text(n_lines, *, error_rate=0.1, seed=0) -> str`:

  - Returns a string of `n_lines` lines, each newline-terminated
    (the last line ends with `\\n` too).
  - Timestamps start at "2026-01-01T00:00:00" and increment by 1 SECOND
    per line. Use `datetime.isoformat(timespec="seconds")` to format.
  - Levels: ERROR with probability `error_rate`, INFO otherwise.
    Use `random.Random(seed)` for determinism.
  - Each line has at least: `path=/api/<i>` and `status=<200|500>`
    (status=500 for ERROR, 200 for INFO).
  - Format ALWAYS:  "<ts> <LEVEL> path=/api/<i> status=<status>\\n"

Hidden tests in 04_solo_test.py.
"""
import random
from datetime import datetime, timedelta


def make_log_text(n_lines: int, *, error_rate: float = 0.1, seed: int = 0) -> str:
    raise NotImplementedError
