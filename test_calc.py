import pytest
from calc import Calc


def test_calc():
    assert 1 == 1


def test_get_minus():
    cases = [(4, 3, 1), (3, 4, -1), (10, 10, 0)]
    calc = Calc()

    for case in cases:
        ret = calc.get_minus(case[0], case[1])
        assert ret == case[2]
