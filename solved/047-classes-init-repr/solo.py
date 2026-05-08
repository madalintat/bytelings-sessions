"""Rung 4: Solo — solved version.

`Email.__init__` normalises (strip + lower) before validating so the
rules apply to the canonical form, not whatever whitespace the caller
passed. Counting `@` with `address.count("@") != 1` rejects both
zero and multiple `@` signs in one check.
"""


class Email:
    def __init__(self, address: str) -> None:
        cleaned = address.strip().lower()
        if not cleaned:
            raise ValueError("email address must not be empty")
        if cleaned.count("@") != 1:
            raise ValueError(f"email must contain exactly one '@': {cleaned!r}")
        self.address = cleaned

    def __repr__(self) -> str:
        return f"Email({self.address!r})"

    def domain(self) -> str:
        return self.address.split("@")[1]
