"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.


def func(a, b):
    return (a ** b) ** 2


cache_func = cache(func)

some = 100, 200

val_1 = cache_func(*some)
val_2 = cache_func(*some)

assert val_1 is val_2

"""
import functools
from typing import Callable


def cache(func: Callable) -> Callable:
    cached_val = {}

    @functools.wraps(func)
    def decorator(*args, **kwargs):
        decorator.called = 0
        key = args + tuple(sorted(kwargs.items()))
        if key not in cached_val:
            cached_val[key] = func(*args, **kwargs)
        decorator.called += 1
        return cached_val[key]

    return decorator
