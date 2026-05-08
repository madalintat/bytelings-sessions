"""Rung 4: Solo — solved version.

`BookNotFound` and `AlreadyCheckedOut` carry domain data as attributes
so callers can act on them (e.g. show which book or who has it).
`checkout` is EAFP: we attempt `catalog[isbn]` and let `KeyError`
guide us to `BookNotFound`. We then check `borrower` and raise
`AlreadyCheckedOut` if the book is already out.
"""


class LibraryError(Exception):
    pass


class BookNotFound(LibraryError):
    def __init__(self, isbn: str) -> None:
        self.isbn = isbn
        super().__init__(f"book not found: {isbn}")


class AlreadyCheckedOut(LibraryError):
    def __init__(self, isbn: str, borrower: str) -> None:
        self.isbn = isbn
        self.borrower = borrower
        super().__init__(f"already checked out: {isbn}")


def checkout(catalog: dict, isbn: str, by: str) -> dict:
    try:
        record = catalog[isbn]
    except KeyError:
        raise BookNotFound(isbn)
    if record["borrower"] is not None:
        raise AlreadyCheckedOut(isbn, record["borrower"])
    record["borrower"] = by
    return record
