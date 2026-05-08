"""Rung 4: Solo implement — solved version.

Dispatch-by-dict (P-04): map rule_id to a lambda that reads the right
threshold key from config and compares the provided metric.
Unknown rule IDs fall through to False without raising.
"""
from __future__ import annotations

from typing import Any

# Map each rule_id to a function (config, *args) -> bool.
_THRESHOLD_CHECKS: dict[str, Any] = {
    "function-too-long": lambda cfg, count: count > cfg["function-too-long-max"],
    "nested-loop-depth": lambda cfg, depth: depth > cfg["nested-loop-depth-max"],
}


def apply_threshold(rule_id: str, config: dict, *args) -> bool:
    """Return True if the finding should fire given `config` thresholds."""
    check = _THRESHOLD_CHECKS.get(rule_id)
    if check is None:
        return False
    return check(config, *args)
