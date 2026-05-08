"""Tests for rung 3."""
import importlib.util
from pathlib import Path

from _byte import diagnose

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def _count(result):
    return len(result)


def _valid(result):
    """All activities in result are non-overlapping."""
    sorted_r = sorted(result, key=lambda a: a[1])
    for i in range(1, len(sorted_r)):
        if sorted_r[i][0] < sorted_r[i - 1][1]:
            return False
    return True


def test_basic():
    # Classic 11-activity instance from CLRS; greedy finds 4.
    acts = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9),
            (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]
    result = ex.select_activities(acts)
    diagnose(
        _count(result) == 4 and _valid(result),
        f"Expected 4 non-overlapping activities, got {result!r}.",
        (lambda: not _valid(result),
         "Some activities in your result overlap. Make sure you only add an"
         " activity when its start >= last_finish."),
        (lambda: _count(result) < 4,
         "You found fewer than 4 activities. Did you sort by finish time?"
         " Sorting by start time is the classic mistake here."),
    )


def test_empty():
    assert ex.select_activities([]) == []


def test_one():
    result = ex.select_activities([(0, 5)])
    assert result == [(0, 5)]


def test_all_overlap():
    acts = [(0, 10), (1, 11), (2, 12)]
    result = ex.select_activities(acts)
    diagnose(
        _count(result) == 1,
        f"All activities fully overlap; expected 1, got {result!r}.",
        (lambda: _count(result) > 1,
         "You selected more than one activity but they all overlap each other."
         " Only one can be chosen."),
    )


def test_back_to_back():
    acts = [(0, 1), (1, 2), (2, 3), (3, 4)]
    result = ex.select_activities(acts)
    diagnose(
        _count(result) == 4,
        f"Back-to-back activities should all be selectable; got {result!r}.",
        (lambda: _count(result) == 3,
         "You excluded one back-to-back activity. The condition is start >="
         " last_finish, not strictly greater. An activity starting exactly when"
         " the previous one finishes is compatible."),
    )


def test_long_blocks_short():
    """Classic exchange-argument demo: long meeting loses to three shorts."""
    acts = [(0, 100), (1, 2), (2, 3), (3, 4)]
    result = ex.select_activities(acts)
    diagnose(
        _count(result) == 3 and _valid(result),
        f"Expected 3 short activities (not the long one), got {result!r}.",
        (lambda: (0, 100) in result and _count(result) == 1,
         "You chose the activity finishing at 100. Sorting by finish time gives"
         " the three short activities instead — that's three, not one."),
    )
