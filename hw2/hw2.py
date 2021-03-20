"""
Given an array of size n, find the most common and the least common elements.
The most common element is the element that appears more than n // 2 times.
The least common element is the element that appears fewer than other.

You may assume that the array is non-empty and the most common element
always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3, 2

Example 2:

Input: [2,2,1,1,1,2,2]
Output: 3, 2

"""
from collections import Counter
from typing import List, Tuple


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    """
    >>> major_and_minor_elem([3,2,3])
    [3, 2]
    >>> major_and_minor_elem([2,2,1,1,1,2,2])
    [2, 1]
    >>> major_and_minor_elem([0,0,0,0,1,1])
    [0, 1]
    """
    maj_min = []
    conter = Counter(inp)
    return conter.most_common()[0][0], conter.most_common()[-1][0]
