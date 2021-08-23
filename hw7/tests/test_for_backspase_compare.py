import pytest

from hw7.hw2 import backspace_compare


@pytest.mark.parametrize(
    ["string_1", "string_2", "expected_result"],
    [
        ("ab#c", "ad#c", True),
        ("a##c", "#a#c", True),
        ("a#c", "b", False),
        ("###", "###", True),
    ],
)
def test_homework_class(string_1, string_2, expected_result):
    assert backspace_compare(string_1, string_2) == expected_result
