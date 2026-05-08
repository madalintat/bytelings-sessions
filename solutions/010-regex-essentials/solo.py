"""Rung 4: Solo implement.

Topic: extract every email address from a chunk of text

Implement `find_emails(text)`:

- Return a list of email-like substrings, in order of appearance.
- An email is: one or more 'word' chars, dots, hyphens, plus signs, or
  underscores; followed by '@'; followed by one or more domain labels
  separated by dots; the final label is at least 2 letters.
- Lowercase the matches before returning.

Examples:
    "ping me at Foo@Bar.COM or x@y.io" -> ['foo@bar.com', 'x@y.io']

The tests in 04_solo_test.py are HIDDEN. Don't peek before you try.
"""
import re


def find_emails(text: str) -> list[str]:
    raise NotImplementedError
