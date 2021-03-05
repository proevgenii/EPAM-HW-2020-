"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from sequence import Sequence

data_to_process = [
    0,
    1,
    1,
    2,
    3,
    5,
    8,
    13,
    21,
    34,
    55,
    89,
    144,
    233,
    377,
    610,
    987,
    1597,
    2584,
    4181,
    6765,
]


def check_fibonacci(data: Sequence) -> None:
    if len(data) < 3:
        return False

    a, b, c = data[0], data[1], data[2]
    while data:
        # print(len(data), data[2])
        if not (a + b) == c:
            return False

        if len(data) <= 3:
            break
        data = data[1:]
        a, b, c = b, c, data[2]
    return True
