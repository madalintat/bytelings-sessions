"""Rung 3: Guided — analyze_text.

Topic: EAFP loop + structured logging.

Walk a multi-line string, parse each line, tally the result. The
parser and the custom exception are inlined here for the curriculum
day; in the real `analyzer/` package they'd live in their own modules.
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
    """Walk every line in `text`. Parse what you can, count what you skip.

    Implementation:
      - For each line in `text.splitlines()`:
          * try parse_line(line);
          * on MalformedLine -> agg.skipped += 1, log.debug("skipping ...")
                                and continue;
          * on success -> agg.parsed += 1; agg.levels[rec.level] += 1;
                          if "path" in rec.fields, agg.top_paths[path] += 1.
      - Return the agg.
    """
    # TODO: implement.
    raise NotImplementedError
