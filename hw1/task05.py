"""
Given a list of integers numbers "nums".

You need to find a sub-array with length less equal to "k", with maximal sum.

The written function should return the sum of this sub-array.

Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List

result = []


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    if len(nums) < k:
        return 'Ivalid "k" value '
    while k > 1:
        summ = 0
        for i in range(k):
            summ += nums[i]

        sum_iter = summ
        for j in range(k, len(nums)):
            sum_iter += nums[j] - nums[j - k]
            summ = max(summ, sum_iter)
            result.append(max(summ, sum_iter))

        k = k - 1
    return max(result)
