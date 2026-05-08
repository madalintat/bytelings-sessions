"""Rung 3: Guided — solved version.

`bucket_by_size` classifies strings by length into 'small', 'medium',
or 'large' buckets:
  - `small` and `large` must be keyword-only (a `*` before them in the
    signature, or after the positional args). The test calls
    `bucket_by_size(["a"], 2, 5)` and expects TypeError.
  - Validate `small >= large` upfront to raise ValueError.
  - Build the output dict with all three keys pre-set to empty lists
    so callers always get a stable structure.

The classification logic:
    if len(item) <= small  -> 'small'
    elif len(item) >= large -> 'large'
    else                   -> 'medium'
"""


def bucket_by_size(
    items: list[str], *, small: int, large: int
) -> dict[str, list[str]]:
    """Bucket strings by length.

    >>> bucket_by_size(['hi', 'hello', 'h'], small=2, large=5)
    {'small': ['hi', 'h'], 'medium': [], 'large': ['hello']}
    >>> bucket_by_size([], small=1, large=5)
    {'small': [], 'medium': [], 'large': []}
    """
    if small >= large:
        raise ValueError(f"small ({small}) must be < large ({large})")
    result: dict[str, list[str]] = {"small": [], "medium": [], "large": []}
    for item in items:
        n = len(item)
        if n <= small:
            result["small"].append(item)
        elif n >= large:
            result["large"].append(item)
        else:
            result["medium"].append(item)
    return result
