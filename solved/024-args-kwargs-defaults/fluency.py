"""Rung 2: Fluency — solved version.

Three args/kwargs/defaults fixes:
  1. add_item: mutable default `[]` trap — same as Day 23. Use `None`
     sentinel and create a fresh list inside.
  2. merge_dicts: `return dicts` returns the TUPLE of input dicts, not a
     merged dict. The idiom is `{**d for d in dicts}` → better:
     `{k: v for d in dicts for k, v in d.items()}`. Or simpler using
     dict unpacking with ** in a loop:
     `result = {}; for d in dicts: result.update(d); return result`.
     Cleanest: `{k: v for d in dicts for k, v in d.items()}`.
  3. call_with_extras: `fn(*args)` drops `**kwargs`. The fix is
     `fn(*args, **kwargs)`.
"""


def add_item(item, bucket=None):
    """Append `item` to `bucket` and return it."""
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket


def merge_dicts(*dicts):
    """Merge any number of dicts; later dicts win on key collisions."""
    return {k: v for d in dicts for k, v in d.items()}


def call_with_extras(fn, *args, **kwargs):
    """Call fn(*args, **kwargs) and return its result."""
    return fn(*args, **kwargs)
