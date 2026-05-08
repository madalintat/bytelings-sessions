"""Rung 3: Guided — solved version.

`parse_contact` chains split -> strip each -> pad to length 4 -> unpack:
  1. Split on ';', strip each part.
  2. Pad with empty strings so we always have at least 4 fields (avoids
     index errors on short input).
  3. Unpack into last, first, email, phone.
  4. Build name = (first + " " + last).strip() — strip handles the case
     where first is "" (leaving just last without a leading space).
  5. Email lowercased; phone = only digits from the original field.

Using `extend` to pad is one clean approach. Alternatively, you can
slice with a default: `(fields + ['', '', '', ''])[:4]`.
"""


def parse_contact(line: str) -> dict[str, str]:
    """Parse a semicolon-separated 'Last;First;Email;Phone' line.

    >>> parse_contact("Smith;John;John@Acme.com;+1 (415) 555-1212")
    {'name': 'John Smith', 'email': 'john@acme.com', 'phone': '14155551212'}
    >>> parse_contact("O'Hara;Aoife;aoife@x.io;")
    {'name': "Aoife O'Hara", 'email': 'aoife@x.io', 'phone': ''}
    >>> parse_contact("Solo")
    {'name': 'Solo', 'email': '', 'phone': ''}
    """
    parts = [p.strip() for p in line.split(";")]
    parts.extend([""] * (4 - len(parts)))
    last, first, email, phone = parts[:4]
    name = f"{first} {last}".strip()
    digits = "".join(c for c in phone if c.isdigit())
    return {"name": name, "email": email.lower(), "phone": digits}
