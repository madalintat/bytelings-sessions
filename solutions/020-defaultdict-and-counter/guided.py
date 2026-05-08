"""Rung 3: Guided implement.

Topic: index records by a category

Implement `index_by(records, key)`: take a list of dicts and a key
name; return a dict mapping each value seen for that key to the list
of records sharing it.
"""
from collections import defaultdict


def index_by(records: list[dict], key: str) -> dict:
    """Group records by the value of `records[i][key]`.

    Records that DON'T have `key` are skipped silently.
    Return a plain dict (not a defaultdict).
    Order within each group is the order from `records`.

    >>> rs = [
    ...     {'name': 'a', 'team': 'red'},
    ...     {'name': 'b', 'team': 'blue'},
    ...     {'name': 'c', 'team': 'red'},
    ... ]
    >>> index_by(rs, 'team')
    {'red': [{'name': 'a', 'team': 'red'}, {'name': 'c', 'team': 'red'}], 'blue': [{'name': 'b', 'team': 'blue'}]}

    >>> index_by([{'team': 'x'}, {'no_team': 1}], 'team')
    {'x': [{'team': 'x'}]}

    >>> index_by([], 'team')
    {}
    """
    # TODO: build a defaultdict(list); skip records missing the key.
    raise NotImplementedError
