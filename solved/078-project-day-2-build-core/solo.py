"""Rung 4: Solo — solved version.

analyze_paths reads each file, runs analyze_text, merges aggregates.
OSError is caught per-file with log.warning; processing continues.
Returns an empty Aggregate if no files succeed.
"""
import logging
from functools import reduce
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_g_spec = spec_from_file_location("_g", Path(__file__).parent / "guided.py")
_g = module_from_spec(_g_spec)
_g_spec.loader.exec_module(_g)

Aggregate = _g.Aggregate
analyze_text = _g.analyze_text

log = logging.getLogger(__name__)


def analyze_paths(paths) -> "Aggregate":
    aggregates = []
    for path in paths:
        try:
            text = Path(path).read_text()
        except OSError as e:
            log.warning("could not read %s: %s", path, e)
            continue
        aggregates.append(analyze_text(text))
    if not aggregates:
        return Aggregate()
    return reduce(lambda a, b: a.merge(b), aggregates)
