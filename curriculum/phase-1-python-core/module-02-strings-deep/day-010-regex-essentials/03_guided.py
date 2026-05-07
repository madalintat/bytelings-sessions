"""Rung 3: Guided implement.

Topic: extracting groups from a regex match

Implement `parse_log_line(line)`: parse a line like
'2026-05-08 14:33:21 ERROR something went wrong' into
(date, time, level, message). Use a single regex with capture groups.
"""
import re


def parse_log_line(line: str) -> tuple[str, str, str, str] | None:
    """Parse a log line. Return (date, time, level, message) or None if no match.

    The format is exactly:
        YYYY-MM-DD HH:MM:SS LEVEL message...
    where LEVEL is one of DEBUG, INFO, WARNING, ERROR, CRITICAL.

    >>> parse_log_line("2026-05-08 14:33:21 ERROR boom")
    ('2026-05-08', '14:33:21', 'ERROR', 'boom')
    >>> parse_log_line("nope") is None
    True
    >>> parse_log_line("2026-05-08 14:33:21 INFO hello world")
    ('2026-05-08', '14:33:21', 'INFO', 'hello world')
    """
    # TODO: build a regex with 4 capture groups and use re.fullmatch.
    # If it doesn't match, return None. Otherwise return m.groups().
    raise NotImplementedError
