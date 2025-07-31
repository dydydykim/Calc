import pytest

from calc import Calc


def test_calc():
    assert 1 == 1
    # pytest.fail()


def test_get_divide():
    calc = Calc()
    assert calc.getDivde(5,1) == 5
