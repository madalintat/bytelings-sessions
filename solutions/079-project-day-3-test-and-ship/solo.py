"""Rung 4: Solo — end-to-end test + helper.

Topic: prove the parallel path is equivalent to the serial path.

Implement two things:

1. `make_files(tmp_path, n_files, n_lines, seed=0) -> list[Path]`:
     - Drop `n_files` synthetic .log files into tmp_path.
     - Each file gets `n_lines` lines, ~10% errors (use random.Random(seed)).
     - Format: "<iso_ts> <LEVEL> path=/api/<idx> status=<200|500>".
     - Use a UTC timestamp starting at "2026-01-01T00:00:00", incrementing
       by 1 second per line.
     - Return the list of paths.

2. `triple(paths) -> tuple[Aggregate, Aggregate, bool]`:
     - serial: analyze_paths(paths)  (from day-078 rung 4)
     - parallel: analyze_paths_parallel(paths, max_workers=2)
     - third element: True iff the two aggregates have equal
       parsed, skipped, levels, and top_paths.

Hidden tests in 04_solo_test.py.
"""
import random
from datetime import datetime, timedelta
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

# Serial analyze_paths from yesterday.
_serial_path = (
    Path(__file__).parent.parent
    / "078-project-day-2-build-core"
    / "solo.py"
)
_serial_spec = spec_from_file_location("_serial", _serial_path)
_serial = module_from_spec(_serial_spec)
_serial_spec.loader.exec_module(_serial)

# Today's parallel analyze_paths_parallel.
_par_spec = spec_from_file_location("_par", Path(__file__).parent / "guided.py")
_par = module_from_spec(_par_spec)
_par_spec.loader.exec_module(_par)

analyze_paths = _serial.analyze_paths
analyze_paths_parallel = _par.analyze_paths_parallel


def make_files(tmp_path: Path, n_files: int, n_lines: int, seed: int = 0) -> list[Path]:
    raise NotImplementedError


def triple(paths) -> tuple:
    raise NotImplementedError
