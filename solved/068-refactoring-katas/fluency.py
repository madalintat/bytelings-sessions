"""Rung 2: Fluency drill — solved version.

Extract letter_grade() as a standalone helper, then call it from
grade_summary. Both functions now have a single responsibility.
"""


def letter_grade(score: float) -> str:
    """Return the letter grade for a numeric score."""
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"


def grade_summary(scores: list[int]) -> dict:
    if not scores:
        return {"avg": 0.0, "grade": "F"}
    avg = sum(scores) / len(scores)
    return {"avg": avg, "grade": letter_grade(avg)}
