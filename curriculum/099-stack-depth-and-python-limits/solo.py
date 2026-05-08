"""Rung 4: Solo.

Topic: iterative tree-max — no recursion, arbitrary depth.

Given a tree represented as a dict where each node has the form
    {"value": <int>, "children": [<node>, <node>, ...]}
return the largest value anywhere in the tree.

Use an explicit stack; don't recurse. The tree can be very deep.

>>> max_value({"value": 5, "children": []})
5
>>> max_value({"value": 1, "children": [{"value": 9, "children": []}]})
9

Tests in 04_solo_test.py are HIDDEN.
"""


def max_value(node: dict) -> int:
    raise NotImplementedError
