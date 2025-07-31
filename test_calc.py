import pytest
from calc import Calc

def test_getSumSUm():
    calc = Calc()
    ret = calc.getSumSum(1, 2, 3)
    assert ret == 6