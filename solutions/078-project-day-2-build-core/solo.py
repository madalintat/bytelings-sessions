"""Rung 4: Solo — analyze_paths (serial).

Topic: walk a directory of log files, aggregate.

Implement `analyze_paths(paths) -> Aggregate`:

  - `paths` is a list/iterable of pathlib.Path objects.
  - For each path, read the file and run `analyze_text` on its contents.
  - Merge the per-file aggregates into a single Aggregate.
  - On `OSError` (file vanished, perms, ...) log.warning AND keep going
    — do NOT propagate.
  - Return the merged Aggregate.

This module re-uses analyze_text and Aggregate from rung 3 by importing
03_guided.py.

Hidden tests in 04_solo_test.py.
"""
import logging
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

# Re-use rung 3's parser + analyzer.
_g_spec = spec_from_file_location("_g", Path(__file__).parent / "guided.py")
_g = module_from_spec(_g_spec)
_g_spec.loader.exec_module(_g)

Aggregate = _g.Aggregate
analyze_text = _g.analyze_text

log = logging.getLogger(__name__)


def analyze_paths(paths) -> "Aggregate":
    raise NotImplementedError
