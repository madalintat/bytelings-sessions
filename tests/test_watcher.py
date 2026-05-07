"""Tests for watcher logic that doesn't require real file events."""
from pathlib import Path

from bytelings import watcher


def test_run_pytest_returns_pass_for_passing_test(tmp_path: Path):
    test_file = tmp_path / "ok_test.py"
    test_file.write_text("def test_ok():\n    assert 1 + 1 == 2\n")
    result = watcher.run_pytest(test_file)
    assert result.passed is True


def test_run_pytest_returns_fail_with_summary_for_failing_test(tmp_path: Path):
    test_file = tmp_path / "fail_test.py"
    test_file.write_text("def test_no():\n    assert 1 == 2\n")
    result = watcher.run_pytest(test_file)
    assert result.passed is False
    assert (
        "fail" in result.summary.lower() or "AssertionError" in result.summary
    )


def test_run_pytest_handles_missing_file(tmp_path: Path):
    test_file = tmp_path / "nope.py"
    result = watcher.run_pytest(test_file)
    assert result.passed is False


def test_truncate_to_first_failure_keeps_first_only():
    raw = (
        "FAILED tests/foo.py::test_a - assert 1 == 2\n"
        "FAILED tests/foo.py::test_b - assert 3 == 4\n"
        "FAILED tests/foo.py::test_c - assert 5 == 6\n"
    )
    out = watcher.truncate_to_first_failure(raw)
    assert "test_a" in out
    assert "test_b" not in out  # truncated
