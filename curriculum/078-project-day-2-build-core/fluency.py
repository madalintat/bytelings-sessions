"""Rung 2: Fluency — finish Aggregate.merge.

Topic: combining two Counter-bearing aggregates.

Implement `Aggregate.merge(other) -> Aggregate` so that:
  - parsed and skipped add as ints.
  - levels and top_paths combine as Counter `+` (multiset add).
  - Returns a NEW Aggregate (does not mutate self or other).
"""
from collections import Counter
from dataclasses import dataclass, field


@dataclass
class Aggregate:
    parsed: int = 0
    skipped: int = 0
    levels: Counter = field(default_factory=Counter)
    top_paths: Counter = field(default_factory=Counter)

    def merge(self, other: "Aggregate") -> "Aggregate":
        # TODO: return Aggregate(...) combining the four fields.
        raise NotImplementedError
