"""Rung 3: Guided implement — solved version.

parse_line splits on whitespace, validates the timestamp via
datetime.fromisoformat, checks the level against ALLOWED_LEVELS, and
parses key=value tokens. Any validation failure raises MalformedLine
with a human-readable reason.
"""
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class LogRecord:
    ts: datetime
    level: str
    fields: dict[str, str] = field(default_factory=dict)


class MalformedLine(Exception):
    """Raised when a log line can't be parsed."""

    def __init__(self, line: str, reason: str) -> None:
        super().__init__(f"{reason}: {line!r}")
        self.line = line
        self.reason = reason


ALLOWED_LEVELS = {"DEBUG", "INFO", "WARN", "ERROR"}


def parse_line(line: str) -> LogRecord:
    """Parse one log line into a LogRecord."""
    s = line.strip()
    if not s:
        raise MalformedLine(line, "empty line")
    parts = s.split()
    try:
        ts = datetime.fromisoformat(parts[0])
    except (ValueError, IndexError):
        raise MalformedLine(line, "bad timestamp")
    if len(parts) < 2 or parts[1] not in ALLOWED_LEVELS:
        raise MalformedLine(line, "bad level")
    fields: dict[str, str] = {}
    for tok in parts[2:]:
        if "=" not in tok:
            raise MalformedLine(line, f"bad key=value: {tok}")
        k, v = tok.split("=", 1)
        fields[k] = v
    return LogRecord(ts=ts, level=parts[1], fields=fields)
