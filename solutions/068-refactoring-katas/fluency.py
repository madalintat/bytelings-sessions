"""Rung 2: Fluency drill — extract a helper function.

Topic: refactoring move "extract function".

`grade_summary` is a one-blob function. Extract the
*letter_grade* logic into its own function called `letter_grade(score)`.
Behavior of `grade_summary` must not change (the tests check both).
"""


def grade_summary(scores: list[int]) -> dict:
    if not scores:
        return {"avg": 0.0, "grade": "F"}
    avg = sum(scores) / len(scores)
    # TODO: extract this if-chain into letter_grade(score) -> str
    if avg >= 90:
        grade = "A"
    elif avg >= 80:
        grade = "B"
    elif avg >= 70:
        grade = "C"
    elif avg >= 60:
        grade = "D"
    else:
        grade = "F"
    return {"avg": avg, "grade": grade}


# TODO: define `letter_grade(score: float) -> str` with the same rules
# above, and have grade_summary call it.
