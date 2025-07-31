import pytest
from calc import Calc


def test_calc():
    assert 1==1
    pytest.fai()

def test_getZegop():
    calc= Calc()
    assert calc.getZegop(1) == 1
    assert calc.getZegop(2) == 4
    assert calc.getZegop(3) == 9
    assert calc.getZegop(-1) == 1
    assert calc.getZegop(-2) == 4

