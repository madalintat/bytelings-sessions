"""Rung 4: Solo — solved version.

`merge_rosters` merges two contact lists by id, with secondary winning
on field conflicts:
  1. Build a result dict keyed by id, walking primary first to set order.
  2. For each secondary contact: if the id already exists, merge the dicts
     (primary fields not in secondary are preserved; secondary fields override).
     If the id is new, append it at the end.
  3. Convert to list, preserving insertion order.

The `{**primary_contact, **secondary_contact}` dict-merge idiom is the
cleanest way to overlay: secondary fields overwrite primary fields with
the same name.

Inputs are not mutated: we use `dict(primary_contact)` to copy before
merging.
"""


def merge_rosters(primary: list[dict], secondary: list[dict]) -> list[dict]:
    result: dict[int, dict] = {}
    for c in primary:
        result[c["id"]] = dict(c)
    for c in secondary:
        cid = c["id"]
        if cid in result:
            result[cid] = {**result[cid], **c}
        else:
            result[cid] = dict(c)
    return list(result.values())
