import functools

import pytest

from hw5.save_original_info import custom_sum, print_result


@print_result
def custom_sum(*args):
    """This function can sum any objects which have __add___"""
    return functools.reduce(lambda x, y: x + y, args)


def test_info_saving_decorator():
    assert custom_sum([1, 2, 3], [4, 5]) == [1, 2, 3, 4, 5]
    assert custom_sum(1, 2, 3, 4) == 10
    assert (
        custom_sum.__doc__
        == """This function can sum any objects which have __add___"""
    )
    assert str(custom_sum.__name__) == "custom_sum"
    assert isinstance(custom_sum.__original_func, type(custom_sum))
