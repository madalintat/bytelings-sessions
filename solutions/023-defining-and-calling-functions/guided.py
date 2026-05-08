"""Rung 3: Guided implement.

Topic: a small pure function with type hints and a docstring

Implement `bucket_by_size(items, *, small, large)`:
- Classify items as 'small', 'medium', or 'large' based on length.
- Return a dict {'small': [...], 'medium': [...], 'large': [...]}.
"""


def bucket_by_size(
    items: list[str], small: int, large: int
) -> dict[str, list[str]]:
    """Bucket strings by length.

    Args:
        items: a list of strings.
        small: max length (inclusive) considered "small".
        large: min length (inclusive) considered "large".
                Items in (small, large) are "medium".

    Returns:
        A dict with keys 'small', 'medium', 'large' (each a list,
        possibly empty), preserving original order.

    Raises:
        ValueError: if small >= large.

    Make `small` and `large` keyword-only.

    >>> bucket_by_size(['hi', 'hello', 'h'], small=2, large=5)
    {'small': ['hi', 'h'], 'medium': [], 'large': ['hello']}
    >>> bucket_by_size([], small=1, large=5)
    {'small': [], 'medium': [], 'large': []}
    """
    # TODO: 1) make small/large keyword-only by adjusting the signature.
    # 2) raise ValueError if small >= large.
    # 3) loop, classify by len(item), append to the right bucket.
    raise NotImplementedError
