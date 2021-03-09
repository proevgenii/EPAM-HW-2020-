"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""
import string


def custom_range(rule, start=None, stop=None, step=None):
    outp = []
    if not start:
        start = 0
    else:
        start = rule.index(start)
    if not step:
        step = 1
    stop = rule.index(stop)

    index = list(range(start, stop, step))
    for elem in index:
        outp.append(rule[elem])
    return outp
