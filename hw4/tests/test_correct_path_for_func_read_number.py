import pytest

from hw4.task_1_read_file import read_magic_number


def test_read_file_exceptions():
    """test that exception is raised for non-existing file"""
    with pytest.raises(IOError):
        read_magic_number("non_existing_file.txt")
