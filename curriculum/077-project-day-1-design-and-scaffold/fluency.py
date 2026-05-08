"""Rung 2: Fluency — finish the LogRecord dataclass.

Topic: dataclass with a default-factory field.

The dataclass is mostly there. Add one missing thing: the `fields`
attribute should default to an empty dict. You'll need
`dataclasses.field` and `default_factory=dict`.
"""
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class LogRecord:
    ts: datetime
    level: str
    # TODO: `fields: dict[str, str]` defaulting to {}
    # using dataclasses.field(default_factory=dict).
