"""Rung 4: Solo implement — threshold dispatch.

Topic: dispatch-by-dict (P-04)

Implement `apply_threshold(rule_id, config, *args) -> bool`.

Returns True when the finding EXCEEDS the configured threshold
(i.e. the rule should fire), False otherwise.

Supported rules:
- "function-too-long"
    args: (body_line_count: int,)
    fires when body_line_count > config["function-too-long-max"]

- "nested-loop-depth"
    args: (depth: int,)
    fires when depth > config["nested-loop-depth-max"]

For any unknown rule_id, return False.

Patterns: P-04 (dispatch-by-dict).

Hidden tests verify both rules and the unknown-rule fallback.
"""
from __future__ import annotations


def apply_threshold(rule_id: str, config: dict, *args) -> bool:
    """Return True if the finding should fire given `config` thresholds.

    >>> cfg = {"function-too-long-max": 50, "nested-loop-depth-max": 3}
    >>> apply_threshold("function-too-long", cfg, 51)
    True
    >>> apply_threshold("function-too-long", cfg, 50)
    False
    >>> apply_threshold("nested-loop-depth", cfg, 4)
    True
    """
    raise NotImplementedError
