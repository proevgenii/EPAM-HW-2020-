import pytest

from hw2.hw4 import cache


@cache
def ackermann(m, n):
    ''' just a function for sample'''
    if not m:
        return n + 1
    elif not n:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))


@pytest.mark.parametrize(["m", "n", "number_of_calls"], [(3, 3, 4), (1, 1, 1)])
def test_function_has_called(m, n, number_of_calls):
    ''' this function, checked if decoration function was called'''
    ackermann(m, n)
    assert ackermann.called >= number_of_calls
