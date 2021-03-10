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

    a = data[0]
    b = data[1]
    for i in range(2, len(data)):
        c = data[i]
        print(i, a, b, c)
        if a+b == c:
            c = data[i]
            a, b = b, c
        else:
            return False
    return True
