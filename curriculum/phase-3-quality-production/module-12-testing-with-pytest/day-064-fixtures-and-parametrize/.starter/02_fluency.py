"""Rung 2: Fluency drill — collapse repetitive tests with parametrize.

Topic: pytest.mark.parametrize.

The tested function is fine. The TEST FILE is what's broken — it has
five copy-pasted tests. Open 02_fluency_test.py and replace the five
test functions with ONE parametrized test (the placeholder names it).
"""


def slugify(text: str) -> str:
    """Lowercase, replace runs of non-alphanumerics with single dashes,
    strip leading/trailing dashes."""
    out = []
    prev_dash = True  # treat start-of-string like a leading dash
    for ch in text.lower():
        if ch.isalnum():
            out.append(ch)
            prev_dash = False
        elif not prev_dash:
            out.append("-")
            prev_dash = True
    s = "".join(out)
    return s.rstrip("-")
