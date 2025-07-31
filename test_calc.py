import pytest
from calc import Calc


def test_calc():
    assert 1==1
    pytest.fail()

def test_getZegop():
    calc= Calc()
    assert calc.getZegop(1) == 1
    assert calc.getZegop(2) == 4
    assert calc.getZegop(3) == 9
    assert calc.getZegop(-1) == 1
    assert calc.getZegop(-2) == 4

def test_getSum():
    calc = Calc()
    assert calc.getSum(1, 2) == 3
    assert calc.getSum(1, 0) == 1
    assert calc.getSum(0, 0) == 0
    assert calc.getSum(-1, 1) == 0
    assert calc.getSum(-1, 0) == -1
    assert calc.getSum(-1, -2) == -3
