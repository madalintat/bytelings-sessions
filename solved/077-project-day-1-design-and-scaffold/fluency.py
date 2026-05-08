"""Rung 2: Fluency — solved version.

Add the `fields` attribute with `field(default_factory=dict)` so that
each LogRecord instance gets its own fresh dict rather than sharing a
single mutable default.
"""
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class LogRecord:
    ts: datetime
    level: str
    fields: dict[str, str] = field(default_factory=dict)
