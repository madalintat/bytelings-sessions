"""Rung 2: Fluency drill — rename a function whose name lies.

Topic: renaming as the first step of investigation.

`validate_email` doesn't validate — it MUTATES the input dict by
lowercasing the email field (and returns the dict). That's a lie.

Step 1: rename `validate_email` to `normalize_email_inplace`
        — both in this file and in the test file.
Step 2: keep the body identical.

The tests look for the new name AND check the original name is gone.
"""


def validate_email(record: dict) -> dict:
    record["email"] = record["email"].lower().strip()
    return record
