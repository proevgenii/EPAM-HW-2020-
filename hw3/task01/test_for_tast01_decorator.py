from hw3.task01.task01 import timer

n = 2


@timer(times=n)
def f(*args):
    return args[0]


def test_decorator_called_n_times(arg=1):
    assert f(arg) == arg  # call with args
    assert f() == arg  # First time call without args should return previous args
    assert f() == arg  # Second time call without args should return previous args
    assert f() == None  # Third call without args should return None, cause times=2
