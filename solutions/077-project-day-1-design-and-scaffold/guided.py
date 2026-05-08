"""Rung 3: Guided implement — parse_line.

Topic: parsing one log line into a LogRecord.

Format:
    <iso_ts> <LEVEL> [<key>=<value> ...]

Examples:
    "2026-05-08T10:00:00 INFO path=/users status=200"
    -> LogRecord(ts=datetime(2026,5,8,10,0,0), level="INFO",
                 fields={"path": "/users", "status": "200"})

Allowed levels: DEBUG, INFO, WARN, ERROR.
On any malformed line, raise MalformedLine(line, reason).
"""
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class LogRecord:
    ts: datetime
    level: str
    fields: dict[str, str] = field(default_factory=dict)


class MalformedLine(Exception):
    """Raised when a log line can't be parsed.

    Attributes:
        line: the offending text.
        reason: a short human-readable description.
    """

    def __init__(self, line: str, reason: str) -> None:
        super().__init__(f"{reason}: {line!r}")
        self.line = line
        self.reason = reason


ALLOWED_LEVELS = {"DEBUG", "INFO", "WARN", "ERROR"}


def parse_line(line: str) -> LogRecord:
    """Parse one log line.

    Implementation steps:
      1. Strip the line. If empty -> MalformedLine(line, "empty line").
      2. Split into parts by whitespace.
      3. parts[0] must parse via datetime.fromisoformat — otherwise
         MalformedLine(line, "bad timestamp").
      4. parts[1] must be in ALLOWED_LEVELS — otherwise
         MalformedLine(line, "bad level").
      5. For each part in parts[2:], split on '=' (maxsplit=1). If a
         token has no '=', MalformedLine(line, "bad key=value: <tok>").
      6. Build and return the LogRecord.
    """
    # TODO: implement.
    raise NotImplementedError
