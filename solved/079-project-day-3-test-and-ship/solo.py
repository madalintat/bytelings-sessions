"""Rung 4: Solo — solved version.

make_files drops n_files synthetic .log files into tmp_path.
triple runs both serial and parallel analyzers, returning the two
aggregates and a bool indicating whether they match.

The cross-day imports go through _byte.load_rung so any helpers
defined inside the loaded modules can be picklable across processes
(needed because the parallel path forks workers).
"""
import random
from datetime import datetime, timedelta
from pathlib import Path

from _byte import load_rung

_serial = load_rung(
    Path(__file__).parent.parent / "078-project-day-2-build-core" / "solo.py",
    "_bytelings_d078_solo",
)
_par = load_rung(
    Path(__file__).parent / "guided.py",
    "_bytelings_d079_guided_via_solo",
)

analyze_paths = _serial.analyze_paths
analyze_paths_parallel = _par.analyze_paths_parallel


def make_files(tmp_path: Path, n_files: int, n_lines: int, seed: int = 0) -> list[Path]:
    rng = random.Random(seed)
    start = datetime(2026, 1, 1, 0, 0, 0)
    paths: list[Path] = []
    for f in range(n_files):
        p = tmp_path / f"log-{f}.log"
        lines = []
        for i in range(n_lines):
            ts = (start + timedelta(seconds=f * n_lines + i)).isoformat(timespec="seconds")
            level = "ERROR" if rng.random() < 0.1 else "INFO"
            status = 500 if level == "ERROR" else 200
            lines.append(f"{ts} {level} path=/api/{i % 5} status={status}")
        p.write_text("\n".join(lines) + "\n")
        paths.append(p)
    return paths


def triple(paths) -> tuple:
    serial = analyze_paths(paths)
    parallel = analyze_paths_parallel(paths, max_workers=2)
    match = (
        serial.parsed == parallel.parsed
        and serial.skipped == parallel.skipped
        and serial.levels == parallel.levels
        and serial.top_paths == parallel.top_paths
    )
    return serial, parallel, match
