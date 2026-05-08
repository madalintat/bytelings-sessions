"""Per-assertion diagnostic helper for curriculum test files.

The pattern bytelings steals from Kaggle's `learntools`: when a test
fails, don't just print a generic ``AssertionError``. Map each
*anticipated wrong answer* to a teaching message.

A test author writes a list of (predicate, message) pairs after the
main equality check. If equality fails, the helper walks the pairs in
order and raises the first message whose predicate matches. If no
predicate matches, it falls back to a generic message.

The point: a learner who returns ``"Hello Bytelinger!"`` (no comma)
sees "Your greeting is missing the comma" — not a string diff. Every
wrong answer becomes a teaching moment instead of a "spot the
difference" puzzle.
"""
from __future__ import annotations

from collections.abc import Callable
from typing import TypeAlias

__all__ = ["diagnose", "Check"]

Check: TypeAlias = tuple[Callable[[], bool], str]


def diagnose(passed: bool, fallback_msg: str, *checks: Check) -> None:
    """Assert with a per-wrong-answer diagnostic.

    Args:
        passed: the main pass/fail signal (typically ``actual == expected``).
        fallback_msg: shown when the test fails AND no targeted check fired.
            This should always orient the learner — point at the spec, the
            docstring, or the literal expected value.
        *checks: zero or more ``(predicate, message)`` pairs evaluated in
            order. The first predicate that returns truthy wins; its
            message is raised.

    A predicate that itself raises is treated as "not matching" — we
    swallow and continue. That keeps a flaky predicate from masking a
    real failure.
    """
    if passed:
        return
    for predicate, message in checks:
        try:
            if predicate():
                raise AssertionError(message)
        except AssertionError:
            raise
        except Exception:
            continue
    raise AssertionError(fallback_msg)
