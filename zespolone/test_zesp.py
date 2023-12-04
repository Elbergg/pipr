import pytest
from zesp import Complex_Number


def test_add():
    num1 = Complex_Number(1, 2)
    num2 = Complex_Number(2, 3)
    assert (num1 + num2).rpart == Complex_Number(3, 5).rpart
    assert (num1 + num2).ipart == Complex_Number(3, 5).ipart
    
def test_sub():
    num1 = Complex_Number(1, 2)
    num2 = Complex_Number(2, 3)
    assert (num1 - num2).rpart == Complex_Number(-1, 1).rpart
    assert (num1 - num2).ipart == Complex_Number(-1, -1).ipart

def test_mul():
    num1 = Complex_Number(1, 2)
    num2 = Complex_Number(2, 3)
    assert (num1 * num2).rpart == Complex_Number(-4, 7).rpart
    assert (num1 * num2).ipart == Complex_Number(-4, 7).ipart

def test_rmul():
    num1 = Complex_Number(1, 2)
    num2 = Complex_Number(2, 3)
    assert (num1 * num2).rpart == Complex_Number(-4, 7).rpart
    assert (num1 * num2).ipart == Complex_Number(-4, 7).ipart

def test_couple():
    num = Complex_Number(1, 2)
    assert num.couple().ipart == Complex_Number(1, -2).ipart

def test_truediv():
    num1 = Complex_Number(1, 8)
    num2 = Complex_Number(2, 3)
    assert (num1 / num2).rpart == Complex_Number(2, 1).rpart
    assert (num1 / num2).ipart == Complex_Number(2, 1).ipart

def test_module():
    num1 = Complex_Number(2,2)
    assert num1.module() == 8**(1/2)