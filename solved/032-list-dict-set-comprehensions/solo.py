"""Rung 4: Solo — solved version.

We need to invert the post→tags mapping into tag→posts. The idiomatic
approach is to build the index with `defaultdict(list)` — it handles
the "first time we see a tag" case automatically and lets us skip an
explicit `setdefault` call.

Two loops are needed: one over posts, one over each tag in a post.
After collecting, we sort each list in place because the spec requires
ascending order. Lowercasing is applied at insertion time.
"""
from collections import defaultdict


def tag_index(posts: list[dict]) -> dict[str, list[int]]:
    index: dict[str, list[int]] = defaultdict(list)
    for post in posts:
        for tag in post.get("tags", []):
            index[tag.lower()].append(post["id"])
    for ids in index.values():
        ids.sort()
    return dict(index)
