import pytest

from hw4.task_1_read_file import read_magic_number


def test_read_file_exceptions():
    """test that exception is raised if first line of file contain not a number"""
    with pytest.raises(ValueError):
        read_magic_number("test.txt")
