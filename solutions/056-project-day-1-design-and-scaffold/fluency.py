"""Rung 2: Fluency drill — define the Snapshot dataclass.

Topic: project scaffold

The Snapshot dataclass needs four fields:
    url:         str
    status:      int           (HTTP status code, or 0 for "errored before response")
    body_length: int           (length of the response body in bytes; 0 if errored)
    error:       str | None    (None on success; an error message on failure)

Make it a regular @dataclass (NOT frozen — we may want to mutate during
debugging). Defaults: status=0, body_length=0, error=None.
"""
from dataclasses import dataclass


# TODO: declare the Snapshot dataclass with the four fields above.
@dataclass
class Snapshot:
    url: str
