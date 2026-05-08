"""Rung 2: Fluency drill — count linter findings per rule.

Topic: P-07 accumulator-into-dict (Counter pattern)

Each finding line has the format:
    path:line:col: rule-id: message

Example:
    src/main.py:10:4: bare-except: bare `except:` catches everything

`count_by_rule(text)` should return a dict mapping each rule-id to the
number of times it appears in the findings text.

The BUGGY version below splits on "," instead of ":" — so it never
splits correctly and every line is treated as a single unknown token.

Learner task: fix the two TODOs.
"""
from __future__ import annotations

SAMPLE_FINDINGS = """\
src/main.py:10:4: bare-except: bare `except:` catches everything
src/main.py:22:0: unused-import: `os` imported but never used
src/utils.py:5:8: bare-except: bare `except:` catches everything
src/utils.py:31:0: unused-import: `sys` imported but never used
src/cli.py:14:0: unused-import: `json` imported but never used
"""


def count_by_rule(text: str) -> dict[str, int]:
    """Return {rule_id: count} for all findings in text.

    Blank lines and malformed lines are skipped silently.

    Example:
        >>> count_by_rule("a.py:1:0: bare-except: msg\\na.py:2:0: bare-except: msg\\n")
        {'bare-except': 2}
    """
    counts: dict[str, int] = {}
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        # TODO (fix 1): split on ":" not "," — use line.split(":")
        parts = line.split(",")
        # The rule-id is at index 3 (after path, line-number, col)
        # TODO (fix 2): check len(parts) >= 4 before indexing, strip the value
        rule = parts[3]
        counts[rule] = counts.get(rule, 0) + 1
    return counts
