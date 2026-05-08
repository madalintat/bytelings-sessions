"""Rung 3: Guided implement.

Topic: parse a vendor contact line into a dict

Implement `parse_contact(line)` per the spec.
"""


def parse_contact(line: str) -> dict[str, str]:
    """Parse a semicolon-separated 'Last;First;Email;Phone' line.

    Rules:
        - Split on ';' and strip each field.
        - If fewer than 4 fields, treat missing ones as empty strings.
        - 'name' = first + " " + last, then .strip()
        - 'email' = email lowercased
        - 'phone' = only the digits from the original phone field, in order

    >>> parse_contact("Smith;John;John@Acme.com;+1 (415) 555-1212")
    {'name': 'John Smith', 'email': 'john@acme.com', 'phone': '14155551212'}
    >>> parse_contact("O'Hara;Aoife;aoife@x.io;")
    {'name': 'Aoife O\\'Hara', 'email': 'aoife@x.io', 'phone': ''}
    >>> parse_contact("Solo")
    {'name': 'Solo', 'email': '', 'phone': ''}
    """
    # TODO: split, strip-each, pad, unpack 4, build digits string, return dict.
    raise NotImplementedError
