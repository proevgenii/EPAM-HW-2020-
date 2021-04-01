import pytest

from hw7.hw3 import tic_tac_toe_checker


@pytest.mark.parametrize(
    ["board", "expected_result"],
    [
        ([["o", "o", "o"], ["-", "x", "o"], ["x", "-", "x"]], ("wins o")),
        ([["o", "x", "o"], ["o", "-", "o"], ["-", "x", "x"]], ("unfinished")),
        ([["o", "x", "o"], ["x", "o", "x"], ["x", "o", "x"]], ("draw")),
    ],
)
def test_tic_tac_toe(board, expected_result):
    assert tic_tac_toe_checker(board) == expected_result
