"""Rung 2: Fluency — profile a small analyze_text run.

Topic: cProfile + pstats applied to today's project.

Implement `top_hotspots(text, k) -> list[str]`:

  - Run `analyze_text(text)` under cProfile.Profile().
  - Return the top-k function NAMES (the funcname, not the full key)
    sorted by `tottime`, descending.
  - Skip built-ins (entries whose function name starts with "<").

We import analyze_text and friends from yesterday's rung 3 file.
"""
import cProfile
import io
import pstats
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

analyze_text = _g.analyze_text


def top_hotspots(text: str, k: int = 5) -> list[str]:
    # TODO: profile analyze_text(text), then pull the top-k user functions
    # by tottime. The pstats.Stats `.stats` attribute is a dict where
    # keys are (filename, lineno, funcname); values are
    # (cc, ncalls, tottime, cumtime, callers).
    raise NotImplementedError
