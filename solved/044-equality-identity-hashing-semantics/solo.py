"""Rung 4: Solo — solved version.

We optimistically use a `set` for O(1) membership tests. If we
encounter an unhashable item (TypeError), we fall back to a list
`seen` and switch to O(n) linear checks for that and all subsequent
items. This hybrid strategy handles the mixed-type case cleanly.
"""


def dedupe(items: list) -> list:
    seen_set: set = set()
    seen_list: list | None = None
    result = []
    for item in items:
        if seen_list is not None:
            if item not in seen_list:
                seen_list.append(item)
                result.append(item)
        else:
            try:
                if item not in seen_set:
                    seen_set.add(item)
                    result.append(item)
            except TypeError:
                # item is unhashable — switch to list-based tracking
                seen_list = [i for i in result]
                if item not in seen_list:
                    seen_list.append(item)
                    result.append(item)
    return result
