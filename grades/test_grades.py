import pytest
from grades import Grade, GradingType

def test_grade_compare():
    grading_type1 = GradingType(1, 6)
    grading_type2 = GradingType(1, 3)
    grade1 = Grade(2, grading_type1)
    grade2 = Grade(2, grading_type2)
    assert (grade1 < grade2) is True

def test_create_wrong_grade():
    with pytest.raises(ValueError):
        grading_type1 = GradingType(1, 6, 1)
        grade1 = Grade(2.5, grading_type1)

def test_create_good_grade():
    grading_type1 = GradingType(1, 6, 1)
    grade1 = Grade(2, grading_type1)

def test_create_grade_half_interval():
    grading_type1 = GradingType(1, 6, 0.5)
    grade1 = Grade(2.5, grading_type1) 

def test_create_wrong_grade_half_interval():
    with pytest.raises(ValueError):
        grading_type1 = GradingType(1, 6, 0.5)
        grade1 = Grade(2.7, grading_type1)    

def test_create_wrong_grade():
    with pytest.raises(ValueError):
        grading_type1 = GradingType(1, 6, 0.5)
        grade1 = Grade(10, grading_type1)
                 