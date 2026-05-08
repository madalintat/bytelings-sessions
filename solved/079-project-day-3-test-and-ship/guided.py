"""Rung 3: Guided — solved version.

_analyze_one_path reads one file and returns its Aggregate (empty on
OSError). analyze_paths_parallel maps it across paths via
ProcessPoolExecutor, then reduces with Aggregate.merge.

The module-alias + fork-context dance below is curriculum boilerplate.
The curriculum's dynamic loader names this module
`_079-project-day-3-test-and-ship_rung_3` — illegal Python identifier.
We register an alias under a legal name and pin start method to
"fork" so worker processes inherit the parent's sys.modules. Real
production code with normal module names doesn't need either.
"""
import multiprocessing
import sys
from concurrent.futures import ProcessPoolExecutor
from functools import reduce
from pathlib import Path

from _byte import load_rung

_LEGAL_NAME = "_bytelings_d079_guided"
sys.modules[_LEGAL_NAME] = sys.modules[__name__]
__name__ = _LEGAL_NAME

_g_path = (
    Path(__file__).parent.parent
    / "078-project-day-2-build-core"
    / "guided.py"
)
_g = load_rung(_g_path, "_bytelings_d078_guided")

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
    ctx = multiprocessing.get_context("fork")
    with ProcessPoolExecutor(max_workers=max_workers, mp_context=ctx) as pool:
        partials = list(pool.map(_analyze_one_path, path_list))
    return reduce(lambda a, b: a.merge(b), partials, Aggregate())
