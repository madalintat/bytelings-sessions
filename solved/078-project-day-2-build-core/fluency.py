"""Rung 2: Fluency — solved version.

Aggregate.merge creates a new Aggregate summing the int fields and
using Counter addition (which is multiset union) for the Counter fields.
Neither self nor other is mutated.
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
        return Aggregate(
            parsed=self.parsed + other.parsed,
            skipped=self.skipped + other.skipped,
            levels=self.levels + other.levels,
            top_paths=self.top_paths + other.top_paths,
        )
