import pytest

from hw1.task04 import check_sum_of_four


@pytest.mark.parametrize(
    ["a", "b", "c", "d", "expected_result"],
    [
        ([1, 2], [1, 2], [1, 2], [1, 2], 0),
        ([0, 0], [0, 0], [0, 0], [0, 0], 16),
    ],
)
def test_check_sum_of_four(a, b, c, d, expected_result):
    assert check_sum_of_four(a, b, c, d) == expected_result
