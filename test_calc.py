import pytest
from Calc.calc import Calc

def test_calc():
    assert 1==1
    pytest.fai()

def test_get_sum():
    calc = Calc()
    assert calc.getSum(1, 1) == 2