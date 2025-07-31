import pytest

from calc import Calc


def test_calc():
    assert 1 == 1
    pytest.fail()


def test_getgop():
    calc = Calc()
    assert calc.getGop(2, 3) == 6
