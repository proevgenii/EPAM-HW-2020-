"""
Classic task, a kind of walnut for you

Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List

#


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    quantity = 0
    sums_1 = {}
    for i in a:
        for j in b:
            if i + j in sums_1:
                sums_1[i + j] += 1
            else:
                sums_1[i + j] = 1

    for k in c:
        for j in d:
            if -1 * (i + j) in sums_1:
                quantity += sums_1[-1 * (i + j)]

    return quantity
