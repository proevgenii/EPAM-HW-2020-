import pytest

from hw1.task05 import find_maximal_subarray_sum


@pytest.mark.parametrize(
    ["nums", "k", "expected_result"],
    [([1, 3, -1, -3, 5, 3, 6, 7], 3, 16), ([1, 3, -1, -3, 5, 3, 6, 7], 5, 21)],
)
def test_find_maximal_subarray_sum(nums, k, expected_result):
    assert find_maximal_subarray_sum(nums, k) == expected_result
