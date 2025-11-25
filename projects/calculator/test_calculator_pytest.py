from calculator import add, subtract, multiply, divide
import pytest


def test_add():
    assert add(3, 5) == 8
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(10, 4) == 6
    assert subtract(-2, -2) == 0


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 5) == 0


def test_divide():
    assert divide(10, 2) == 5
    assert divide(3, 1) == 3


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)
