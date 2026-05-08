"""Rung 3: Guided — solved version.

The day's README pitches ProcessPoolExecutor for "true parallel" file
analysis. In practice, the curriculum's dynamic loader gives this
module a hyphenated name (`_079-project-day-3-test-and-ship_rung_3`)
that isn't a legal Python import target, so pickling
`_analyze_one_path` to ship to a worker process fails before the work
even starts. ThreadPoolExecutor sidesteps pickling, and since the
work here is dominated by file I/O (read_text → analyze_text on
already-tokenized output), the GIL is barely contended — a thread
pool delivers most of the wallclock win without the lesson-breaking
dependency on cross-process function shipping.

A learner who wants the pure ProcessPoolExecutor lesson should put
the helper in a sibling top-level .py module that's imported by name,
or package the curriculum properly. That's outside today's scope.
"""
from concurrent.futures import ThreadPoolExecutor
from functools import reduce
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_g_path = (
    Path(__file__).parent.parent
    / "078-project-day-2-build-core"
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
    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        partials = list(pool.map(_analyze_one_path, path_list))
    return reduce(lambda a, b: a.merge(b), partials, Aggregate())
