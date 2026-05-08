"""Rung 3: Guided — analyze_paths_parallel.

Topic: ProcessPoolExecutor over files + reduce(Aggregate.merge).

Implementation steps:
  1. Define `_analyze_one_path(path: Path) -> Aggregate` at module level
     (must be picklable). Read text, run analyze_text. On OSError,
     return an empty Aggregate (skip silently for now — this rung is
     about plumbing, not error handling, which yesterday covered).
  2. In `analyze_paths_parallel(paths, max_workers=None)`:
       - Open a ProcessPoolExecutor.
       - pool.map(_analyze_one_path, list(paths)).
       - functools.reduce(Aggregate.merge, partials, Aggregate()).
"""
from concurrent.futures import ProcessPoolExecutor
from functools import reduce
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

# Import yesterday's analyze_text + Aggregate.
_g_path = (
    Path(__file__).parent.parent
    / "day-078-project-day-2-build-core"
    / "03_guided.py"
)
_g_spec = spec_from_file_location("_g", _g_path)
_g = module_from_spec(_g_spec)
_g_spec.loader.exec_module(_g)

Aggregate = _g.Aggregate
analyze_text = _g.analyze_text


def _analyze_one_path(path: Path) -> "Aggregate":
    # TODO: read the file, return analyze_text(text).
    # On OSError, return an empty Aggregate.
    raise NotImplementedError


def analyze_paths_parallel(paths, max_workers: int | None = None) -> "Aggregate":
    # TODO: use ProcessPoolExecutor + pool.map + reduce(Aggregate.merge, ...).
    raise NotImplementedError
