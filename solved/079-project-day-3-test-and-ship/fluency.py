"""Rung 2: Fluency — solved version.

top_hotspots profiles analyze_text under cProfile, then reads the
.stats dict to find the top-k user-defined functions by tottime.
Entries whose funcname starts with "<" are built-ins/internals — skip them.
"""
import cProfile
import io
import pstats
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

analyze_text = _g.analyze_text


def top_hotspots(text: str, k: int = 5) -> list[str]:
    with cProfile.Profile() as pr:
        analyze_text(text)

    # pstats.Stats(pr).stats is a dict keyed by
    # (filename, lineno, funcname) → (cc, ncalls, tottime, cumtime, callers).
    entries = [
        (funcname, tt)
        for (_filename, _lineno, funcname), (_cc, _nc, tt, _ct, _callers)
        in pstats.Stats(pr).stats.items()
        if not funcname.startswith("<")
    ]
    entries.sort(key=lambda e: e[1], reverse=True)
    return [name for name, _ in entries[:k]]
