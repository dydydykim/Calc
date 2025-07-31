import pytest
from calc import Calc

def test_calc():
    assert 1 == 1


def test_get_divide():
    calc = Calc()
    assert calc.getDivde(5,1) == 5

      
def test_get_minus():
    cases = [(4, 3, 1), (3, 4, -1), (10, 10, 0)]
    calc = Calc()

    for case in cases:
        ret = calc.get_minus(case[0], case[1])
        assert ret == case[2]
        
def test_getgop():
    calc = Calc()
    assert calc.getGop(2, 3) == 6

    
def test_getZegop():
    calc= Calc()
    assert calc.getZegop(1) == 1
    assert calc.getZegop(2) == 4
    assert calc.getZegop(3) == 9
    assert calc.getZegop(-1) == 1
    assert calc.getZegop(-2) == 4