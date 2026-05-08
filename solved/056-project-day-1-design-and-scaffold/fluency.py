"""Rung 2: Fluency — solved version.

`Snapshot` is a regular (mutable) `@dataclass`. The four fields are
declared with the specified types and defaults: `status=0`,
`body_length=0`, `error=None`. `url` has no default so it must be
passed positionally.
"""
from dataclasses import dataclass


@dataclass
class Snapshot:
    url: str
    status: int = 0
    body_length: int = 0
    error: str | None = None
