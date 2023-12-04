import pytest
from box import BoundingBox

def test_calculate_area():
    box = BoundingBox((0,0), (10, 10))
    assert box.calculate_area() == 100

def test_create_box_negative_value():
    with pytest.raises(ValueError):
        box = BoundingBox((-1,-1), (10, 10))

def test_create_box_too_big_value():
    with pytest.raises(ValueError):
        box = BoundingBox((0,0), (1025, 10))

def test_intersection():
    box = BoundingBox((0,0), (10,10))
    box2 = BoundingBox((0,1), (10,11))
    assert box.calculate_intersection(box2) == 90

def test_wrong_intersection():
    box = BoundingBox((0,0), (2,2))
    box2 = BoundingBox((3,3), (4,4))
    assert box.calculate_intersection(box2) == 0

def test_calculate_sum():
    box = BoundingBox((0,0), (2,2))
    box2 = BoundingBox((1,1), (3,3))
    assert box.calculate_sum(box2) == 7

def test_calculate_int_over_un():
    box = BoundingBox((0,0), (10,10))
    box2 = BoundingBox((0,1), (10,11))
    assert box.calculate_int_over_un(box2) == pytest.approx(0.81, 0.82)

def test_calculate_f1():
    box = BoundingBox((0,0), (10,10))
    box2 = BoundingBox((0,1), (10,11))
    assert box.calculate_f1(box2) == 0.90

def test_str():
    box = BoundingBox((0,0), (10,10))
    assert str(box)  == f'lewy dolny wierzcholek: (0, 0), prawy gorny wierzcholek (10, 10)'
     




