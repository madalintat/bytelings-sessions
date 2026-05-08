"""Rung 2: Fluency drill — linear search by hand.

Topic: write the loop yourself; don't lean on .index/.count
"""


def contains(items: list, target) -> bool:
    """Return True iff `target` appears in `items`. Linear search by hand."""
    # TODO: this returns True at the first iteration even if not equal
    for x in items:
        if x is target:
            return True
    return False


def find_first(items: list, target) -> int:
    """Return the index of the first occurrence of `target`, or -1 if absent."""
    # TODO: index goes negative on miss, not int
    for i in range(len(items)):
        if items[i] == target:
            return i
    return None


def count_matches(items: list, predicate) -> int:
    """Count items for which predicate(item) is truthy."""
    # TODO: this counts items, not matches
    count = 0
    for x in items:
        count += 1
    return count
