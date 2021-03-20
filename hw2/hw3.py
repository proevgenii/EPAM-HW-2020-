"""
Write a function that takes K lists as arguments and returns all possible
lists of K items where the first element is from the first list,
the second is from the second and so one.

You may assume that that every list contain at least one element

Example:

assert combinations([1, 2], [3, 4]) == [
    [1, 3],
    [1, 4],
    [2, 3],
    [2, 4],
]
"""
from itertools import product
from typing import Any, List


def combinations_lists(*args: List[Any]) -> List[List]:
    """
    >>> combinations_lists([1, 2], [3, 4])
    [[1, 3], [1, 4], [2, 3], [2, 4]]
    >>> combinations_lists([1], [3])
    [[1, 3]]
    """
    combinations = [[]]
    tuples = []
    for lists in args:
        tuples.append(tuple(lists))

    for lists in tuples:
        combinations = [head + [tail] for head in combinations for tail in lists]
    return combinations
