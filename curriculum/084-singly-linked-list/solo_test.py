"""HIDDEN tests for rung 4."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def _build(values):
    head = None
    for v in reversed(values):
        head = ex.Node(v, head)
    return head


def _to_list(head):
    out = []
    while head is not None:
        out.append(head.value)
        head = head.next
    return out


def test_empty():
    assert ex.reverse(None) is None


def test_single():
    head = _build([42])
    new_head = ex.reverse(head)
    assert _to_list(new_head) == [42]


def test_two():
    head = _build([1, 2])
    new_head = ex.reverse(head)
    assert _to_list(new_head) == [2, 1]


def test_many():
    head = _build([1, 2, 3, 4, 5])
    new_head = ex.reverse(head)
    assert _to_list(new_head) == [5, 4, 3, 2, 1]


def test_does_not_create_new_nodes():
    """Reversing should reuse the existing nodes, not allocate new ones."""
    head = _build([1, 2, 3])
    original_ids = set()
    cur = head
    while cur is not None:
        original_ids.add(id(cur))
        cur = cur.next
    new_head = ex.reverse(head)
    new_ids = set()
    cur = new_head
    while cur is not None:
        new_ids.add(id(cur))
        cur = cur.next
    assert original_ids == new_ids
