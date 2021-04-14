from typing import Tuple

import pytest

from hw1.task03 import find_maximum_and_minimum


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ("test.txt", (1, 4)),
        ("test1.txt", (0, 5)),
    ],
)
def test_find_maximum_and_minimum(value: str, expected_result: Tuple[int, int]):
    assert find_maximum_and_minimum(value) == expected_result
