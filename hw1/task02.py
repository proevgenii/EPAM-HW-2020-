"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from sequence import Sequence


def check_fibonacci(data: Sequence) -> None:
    if len(data) < 3:
        return False

    n = int(len(data)/3)
    a = data[::3]
    b = data[1::3]
    c = data[2::3]
    for i in range(n):
        if not a[i]+b[i] == c[i]:
            return False
        else:
            return True
