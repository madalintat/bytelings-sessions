"""Rung 2: Fluency drill — solved version.

Rename validate_email to normalize_email_inplace to reflect what the
function actually does (mutate in place, not validate).
"""


def normalize_email_inplace(record: dict) -> dict:
    record["email"] = record["email"].lower().strip()
    return record
