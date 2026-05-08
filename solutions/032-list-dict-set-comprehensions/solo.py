"""Rung 4: Solo implement. No scaffold beyond the spec.

Topic: nested comprehension over a list of dicts

Implement `tag_index(posts)`. Each post is a dict like:
    {"id": 7, "tags": ["python", "Async"]}

Return a dict mapping each lowercased tag to the sorted list of post
ids that carry it.

- Tags are case-insensitive ("Async" and "async" are the same tag).
- A post with no tags contributes nothing.
- Posts may share tags. The lists in the result must be sorted ascending.

The tests in 04_solo_test.py are HIDDEN. Don't peek before you try.

Patterns: P-12 (filter-then-map), P-13 (enumerate-for-index), P-14 (zip-parallel-walk).
"""


def tag_index(posts: list[dict]) -> dict[str, list[int]]:
    raise NotImplementedError
