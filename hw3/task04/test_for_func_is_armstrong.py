import pytest
from hw3.task04.task04 import is_armstrong


@pytest.mark.parametrize(
    ["number", "expected_result"],
    [
        (153, True),
        (10, False),
        (9, True),
        (0, True),
        (1, True),
    ],
)
def test_for_func_is_armstrong(number, expected_result):
    assert is_armstrong(number) == expected_result
