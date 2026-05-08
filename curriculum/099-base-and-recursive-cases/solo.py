"""Rung 4: Solo implement.

Topic: count files in a nested directory structure (recursion on trees)

Implement `count_files(tree)` where `tree` is a dict that represents a
directory. Each key is a name; each value is either:
- a string (treat as a file)
- another dict (a subdirectory, recurse into it)

Return the total number of files anywhere in the tree.

Example:
    tree = {
        "readme.md": "file",
        "src": {
            "main.py": "file",
            "lib": {"util.py": "file", "data.json": "file"},
        },
        "empty": {},
    }
    count_files(tree) == 4

The tests in 04_solo_test.py are HIDDEN. Try without peeking.

Patterns: P-28 (memoize-recursive).
"""


def count_files(tree: dict) -> int:
    raise NotImplementedError
