"""Rung 3: Guided implement — string-building the fast way.

Topic: avoid quadratic string concatenation.

Real-world framing: a tiny report formatter that takes (label, value)
pairs and produces "label1=v1; label2=v2; ..." for a log line.

Implementation:
  1. Build the parts as a list of strings.
  2. Use `"; ".join(parts)`.
  3. Do NOT use `result += part` in a loop.

A perf test confirms 100K pairs format in << 1 second.
"""


def format_pairs(pairs: list[tuple[str, str]]) -> str:
    """Return 'k1=v1; k2=v2; ...' or '' if pairs is empty."""
    # TODO: build a list, then join with "; ".
    raise NotImplementedError
