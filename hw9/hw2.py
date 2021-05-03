"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.

>>> with supressor(IndexError):
...    [][2]

"""
from contextlib import contextmanager


@contextmanager
def supressor(er_name):
    try:
        yield er_name
    except er_name:
        pass


class Suppressor:
    def __init__(self, er_name):
        self.er_name = er_name

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        return issubclass(exc_type, self.er_name) or self.er_name is exc_type
