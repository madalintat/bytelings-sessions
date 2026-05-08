"""HIDDEN tests for rung 4."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def _build(values):
    """Standard BST insert."""
    root = None

    def ins(node, x):
        if node is None:
            return ex._Node(x)
        if x < node.value:
            node.left = ins(node.left, x)
        elif x > node.value:
            node.right = ins(node.right, x)
        return node

    for v in values:
        root = ins(root, v)
    return root


def test_empty():
    assert ex.range_query(None, 1, 5) == []


def test_full_range():
    root = _build([5, 3, 7, 1, 4, 6, 8])
    assert ex.range_query(root, 0, 100) == [1, 3, 4, 5, 6, 7, 8]


def test_middle_range():
    root = _build([5, 3, 7, 1, 4, 6, 8])
    assert ex.range_query(root, 3, 6) == [3, 4, 5, 6]


def test_below_all():
    root = _build([5, 3, 7])
    assert ex.range_query(root, -10, 0) == []


def test_above_all():
    root = _build([5, 3, 7])
    assert ex.range_query(root, 100, 200) == []


def test_single_match():
    root = _build([5, 3, 7])
    assert ex.range_query(root, 7, 7) == [7]


def test_lo_equals_hi_no_match():
    root = _build([5, 3, 7])
    assert ex.range_query(root, 4, 4) == []


def test_lower_bound_inclusive():
    root = _build([5, 3, 7, 1, 4])
    assert ex.range_query(root, 4, 5) == [4, 5]
