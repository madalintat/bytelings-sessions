"""Tests for bytelings.testing.diagnose — the per-assertion teach-message helper."""
import pytest

from bytelings.testing import diagnose


def test_passes_silently_when_main_check_passes():
    diagnose(True, "fallback should not appear")
    # No exception = test passes.


def test_raises_fallback_when_no_predicate_fires():
    with pytest.raises(AssertionError, match="orient at the spec"):
        diagnose(False, "orient at the spec")


def test_first_matching_predicate_wins():
    actual = "Hello Bytelinger!"  # missing comma
    with pytest.raises(AssertionError, match="missing the comma"):
        diagnose(
            False,
            "Expected 'Hello, Bytelinger!'.",
            (lambda: ", " not in actual, "Your greeting is missing the comma."),
            (lambda: not actual.endswith("!"), "Your greeting is missing the !."),
        )


def test_predicate_order_matters_first_truthy_wins():
    # Both predicates return True; first should be the one raised.
    with pytest.raises(AssertionError, match="^FIRST$"):
        diagnose(
            False,
            "fallback",
            (lambda: True, "FIRST"),
            (lambda: True, "SECOND"),
        )


def test_skips_predicates_when_main_passed():
    """A truthy main signal short-circuits — predicates with side
    effects must NOT run."""
    side_effects: list[str] = []
    diagnose(
        True,
        "fallback",
        (lambda: side_effects.append("ran") or True, "should not raise"),
    )
    assert side_effects == []


def test_predicate_that_itself_raises_is_skipped_not_propagated():
    """A flaky predicate must NOT mask another predicate or the fallback."""

    def boom() -> bool:
        raise RuntimeError("oops")

    with pytest.raises(AssertionError, match="real reason"):
        diagnose(
            False,
            "fallback",
            (boom, "should not be raised because predicate exploded"),
            (lambda: True, "real reason"),
        )


def test_fallback_used_when_predicates_all_false():
    actual = "totally unrelated wrong answer"
    with pytest.raises(AssertionError, match="Expected.*totally unrelated"):
        diagnose(
            False,
            f"Expected 'Hello, Bytelinger!', got {actual!r}.",
            (lambda: ", " not in "Hello, World!", "ignored — predicate is false"),
        )
