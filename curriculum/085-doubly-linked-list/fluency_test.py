"""Tests for rung 2."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "02_fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_link_sets_both_pointers():
    a = ex.Node("a")
    b = ex.Node("b")
    ex.link(a, b)
    assert a.next is b
    assert b.prev is a


def test_unlink_bypasses_in_both_directions():
    a, b, c = ex.Node("a"), ex.Node("b"), ex.Node("c")
    ex.link(a, b)
    ex.link(b, c)
    ex.unlink(b)
    assert a.next is c
    assert c.prev is a


def test_unlink_long_chain():
    nodes = [ex.Node(i) for i in range(5)]
    for i in range(4):
        ex.link(nodes[i], nodes[i + 1])
    ex.unlink(nodes[2])
    assert nodes[1].next is nodes[3]
    assert nodes[3].prev is nodes[1]
