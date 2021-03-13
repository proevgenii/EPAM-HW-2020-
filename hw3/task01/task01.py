import functools
from typing import Callable


def timer(times):
    def cache(func) -> Callable:
        cached_val = {}

        @functools.wraps(func)
        def decorator(*args):
            if not args:
                args = sorted(cached_val.keys())[-1]
                if decorator.n_calls < times:
                    decorator.n_calls += 1
                    key = args
                    if key not in cached_val:
                        res = func(*args)
                        cached_val[key] = res
                    return cached_val[key]
            else:
                key = args
                if key not in cached_val:
                    res = func(*args)
                    cached_val[key] = res
                return cached_val[key]

        decorator.n_calls = 0
        return decorator

    return cache
