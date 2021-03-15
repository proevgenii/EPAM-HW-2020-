import pytest

from hw4.task_2_mock_input import count_dots_on_i


def test_request_function_exceptions():
    """test that exception is raised for Unreachable url"""
    with pytest.raises(ValueError):
        count_dots_on_i("Unreachable.url")
