import pytest
from fraction import Fraction

def test_create_fraction():
    fraction = Fraction(2, 4)
    assert fraction.numerator == 1
    assert fraction.denominator == 2

def test_add():
    fraction = Fraction(2, 4)
    fraction2 = Fraction(1, 3)
    assert (fraction + fraction2).numerator == 5
    assert (fraction + fraction2).denominator == 6

def test_sub():
    fraction = Fraction(2, 4)
    fraction2 = Fraction(1, 3)
    assert (fraction - fraction2).numerator == 1
    assert (fraction - fraction2).denominator == 6

def test_mul():
    fraction = Fraction(2, 4)
    fraction2 = Fraction(2, 3)
    assert (fraction * fraction2).numerator == 1
    assert (fraction * fraction2).denominator == 3

def test_add_constant():
    fraction = Fraction(2, 4)
    assert fraction.add_constant(3).numerator == 7
    assert fraction.add_constant(3).denominator == 2

def test_numerator():
    fraction = Fraction(2, 4)
    assert fraction.get_numerator() == 1

def test_get_denominator():
    fraction = Fraction(2, 4)
    assert fraction.get_denominator() == 2

def test_set_fraction():
    fraction = Fraction(2, 4)
    assert fraction.set(2, 3).numerator == 2
    assert fraction.set(2, 3).denominator == 3

def test_get_value():
    fraction = Fraction(2, 4)
    assert fraction.get_value() == 1/2

def test_str():
    fraction = Fraction(2, 4)
    assert str(fraction) == '1/2'

def test_zero_denominator():
    with pytest.raises(ZeroDivisionError):
        fraction = Fraction(2, 0)

def test_add_zero():
    fraction = Fraction(2, 4)
    fraction2 = Fraction(0, 4)
    assert (fraction + fraction2).numerator == 1
    assert (fraction + fraction2).denominator == 2

def test_sub_zero():
    fraction = Fraction(2, 4)
    fraction2 = Fraction(0, 4)
    assert (fraction - fraction2).numerator == 1
    assert (fraction - fraction2).denominator == 2

def test_sub_zero():
    fraction = Fraction(2, 4)
    fraction2 = Fraction(0, 4)
    assert (fraction*fraction2).is_zero is True 

def test_div_zero():
    fraction = Fraction(2, 4)
    fraction2 = Fraction(0, 4)    
    assert(fraction2/fraction).is_zero  is True

def test_div():
    fraction = Fraction(3, 2)
    fraction2 = Fraction(3, 1)   
    assert(fraction/fraction2).numerator == 1
    assert(fraction/fraction2).denominator == 2

def test_div_by_zero():
    with pytest.raises(ZeroDivisionError):
        fraction = Fraction(3, 2)
        fraction2 = Fraction(0, 1)
        fraction/fraction2

def test_sub_negative():
        fraction = Fraction(3, 2)
        fraction2 = Fraction(2, 1)
        assert (fraction - fraction2).numerator == -1
        assert (fraction - fraction2).denominator == 2
        