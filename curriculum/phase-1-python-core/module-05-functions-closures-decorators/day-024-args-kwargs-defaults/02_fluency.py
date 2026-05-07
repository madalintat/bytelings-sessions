"""Rung 2: Fluency drill — args, kwargs, defaults.

Topic: mutable defaults trap, *args, **kwargs
"""


def add_item(item, bucket=[]):
    """Append `item` to `bucket` and return it.

    If `bucket` isn't given, each call must produce its OWN fresh list.
    Fix the mutable-default bug.
    """
    # TODO: switch to None sentinel
    bucket.append(item)
    return bucket


def merge_dicts(*dicts):
    """Merge any number of dicts; later dicts win on key collisions.

    Use **unpacking. Return a NEW dict; do not mutate inputs.
    """
    # TODO: this returns a tuple, not a merged dict
    return dicts


def call_with_extras(fn, *args, **kwargs):
    """Call fn(*args, **kwargs) and return its result."""
    # TODO: forwards *args but drops **kwargs
    return fn(*args)
