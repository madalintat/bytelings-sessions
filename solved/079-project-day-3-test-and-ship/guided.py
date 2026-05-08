"""Rung 3: Guided — solved version.

_analyze_one_path reads a file and returns an Aggregate (empty on OSError).
analyze_paths_parallel maps it over paths with ProcessPoolExecutor, then
reduces with Aggregate.merge, starting from an empty Aggregate.
"""
from concurrent.futures import ProcessPoolExecutor
from functools import reduce
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_g_path = (
    Path(__file__).parent.parent
    / "day-078-project-day-2-build-core"
    / "guided.py"
)
_g_spec = spec_from_file_location("_g", _g_path)
_g = module_from_spec(_g_spec)
_g_spec.loader.exec_module(_g)

Aggregate = _g.Aggregate
analyze_text = _g.analyze_text


def _analyze_one_path(path: Path) -> "Aggregate":
    try:
        text = Path(path).read_text()
        return analyze_text(text)
    except OSError:
        return Aggregate()


def analyze_paths_parallel(paths, max_workers: int | None = None) -> "Aggregate":
    path_list = list(paths)
    with ProcessPoolExecutor(max_workers=max_workers) as pool:
        partials = list(pool.map(_analyze_one_path, path_list))
    return reduce(lambda a, b: a.merge(b), partials, Aggregate())
