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
        return exc_type is self.er_name


with Suppressor(IndexError):
    [][2]
