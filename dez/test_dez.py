from dez import Magazine, NotEnoughResourcesError
import pytest

def test_order():
    magazine = Magazine(20, 15, 80, 17)
    assert magazine.check_order(10) == '1000ml of glicerine, 3500ml of aloes, 6000ml of alcohol and 500ml of conservant is needed'

def test_order_not_enough():
    with pytest.raises(NotEnoughResourcesError):
        magazine = Magazine(1, 15, 80, 17)
        magazine.check_order(11)

    