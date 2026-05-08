"""Rung 3: Guided — solved version.

analyze_text walks lines with EAFP: try parse_line, catch MalformedLine,
log.debug and continue. Successful parses increment counts and update
the path counter.
"""
import logging
from collections import Counter
from dataclasses import dataclass, field
from datetime import datetime

log = logging.getLogger(__name__)

ALLOWED_LEVELS = {"DEBUG", "INFO", "WARN", "ERROR"}


class MalformedLine(Exception):
    def __init__(self, line: str, reason: str) -> None:
        super().__init__(f"{reason}: {line!r}")
        self.line = line
        self.reason = reason


@dataclass
class LogRecord:
    ts: datetime
    level: str
    fields: dict[str, str] = field(default_factory=dict)


@dataclass
class Aggregate:
    parsed: int = 0
    skipped: int = 0
    levels: Counter = field(default_factory=Counter)
    top_paths: Counter = field(default_factory=Counter)


def parse_line(line: str) -> LogRecord:
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


def analyze_text(text: str) -> Aggregate:
    """Walk every line in `text`, parse what you can, count what you skip."""
    agg = Aggregate()
    for line in text.splitlines():
        try:
            rec = parse_line(line)
        except MalformedLine:
            agg.skipped += 1
            log.debug("skipping malformed: %s", line[:80])
            continue
        agg.parsed += 1
        agg.levels[rec.level] += 1
        if "path" in rec.fields:
            agg.top_paths[rec.fields["path"]] += 1
    return agg
