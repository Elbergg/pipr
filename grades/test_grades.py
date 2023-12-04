import pytest
from grades import Grade, GradingType

def test_grade_compare():
    grading_type1 = GradingType(1, 6)
    grading_type2 = GradingType(1, 3)
    grade1 = Grade(2, grading_type1)
    grade2 = Grade(2, grading_type2)
    assert (grade1 < grade2) is True

    