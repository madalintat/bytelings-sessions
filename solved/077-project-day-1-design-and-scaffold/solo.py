"""Rung 4: Solo — solved version.

make_log_text generates n_lines of synthetic log lines. Timestamps
increment by one second starting from 2026-01-01T00:00:00. Level is
chosen with random.Random(seed) for determinism; status codes and
path follow from the level.
"""
import random
from datetime import datetime, timedelta


def make_log_text(n_lines: int, *, error_rate: float = 0.1, seed: int = 0) -> str:
    rng = random.Random(seed)
    start = datetime(2026, 1, 1, 0, 0, 0)
    lines = []
    for i in range(n_lines):
        ts = (start + timedelta(seconds=i)).isoformat(timespec="seconds")
        if rng.random() < error_rate:
            level = "ERROR"
            status = 500
        else:
            level = "INFO"
            status = 200
        lines.append(f"{ts} {level} path=/api/{i} status={status}\n")
    return "".join(lines)
