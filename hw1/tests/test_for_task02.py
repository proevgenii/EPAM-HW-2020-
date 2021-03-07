import pytest
from sequence import Sequence

from hw1.task02 import check_fibonacci


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ([0, 1, 1], True),
        ([0], False),
        ([1], False),
        (
            [0, 1, 1, 2],
            True,
        ),
    ],
)
def test_check_fibonacci(value: Sequence, expected_result: bool):
    assert check_fibonacci(value) == expected_result
