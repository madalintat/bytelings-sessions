"""Rung 3: Guided — solved version.

`parse_log_line` uses a single regex with 4 named-or-numbered capture
groups. `re.fullmatch` anchors the entire string, so partial matches
(e.g. trailing garbage) return None cleanly.

The pattern breakdown:
  - `(\\d{4}-\\d{2}-\\d{2})` — date
  - ` ` — literal space
  - `(\\d{2}:\\d{2}:\\d{2})` — time
  - ` ` — literal space
  - `(DEBUG|INFO|WARNING|ERROR|CRITICAL)` — level enum (only exact matches)
  - ` ` — literal space
  - `(.+)` — message (one or more chars; `.` doesn't match newline by default)

`m.groups()` returns the 4 captured strings as a tuple, matching the
declared return type.
"""
import re

_LOG_RE = re.compile(
    r"(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) "
    r"(DEBUG|INFO|WARNING|ERROR|CRITICAL) (.+)"
)


def parse_log_line(line: str) -> tuple[str, str, str, str] | None:
    """Parse a log line. Return (date, time, level, message) or None if no match.

    >>> parse_log_line("2026-05-08 14:33:21 ERROR boom")
    ('2026-05-08', '14:33:21', 'ERROR', 'boom')
    >>> parse_log_line("nope") is None
    True
    >>> parse_log_line("2026-05-08 14:33:21 INFO hello world")
    ('2026-05-08', '14:33:21', 'INFO', 'hello world')
    """
    m = _LOG_RE.fullmatch(line)
    if m is None:
        return None
    return m.groups()
