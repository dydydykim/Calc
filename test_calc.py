import pytest
from calc import Calc

def test_calc():
    calc = Calc()
    assert calc is not None

def test_get_minus():
    calc = Calc()
    ret = calc.get_minus(4, 3)
    assert ret == 1