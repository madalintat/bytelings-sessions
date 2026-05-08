"""Rung 3: Guided — solved version.

We check identity first (`a is b`) because it is the strictest
relation. If that fails we fall back to equality. The order matters:
`a is b` implies `a == b` (for sane types), so we do the cheaper
pointer comparison first.
"""


def relation(a, b) -> str:
    """Return 'identical', 'equal', or 'distinct'."""
    if a is b:
        return "identical"
    if a == b:
        return "equal"
    return "distinct"
