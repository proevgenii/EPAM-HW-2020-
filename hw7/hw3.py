"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"

Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"

    [[-, -, o],
     [-, o, o],
     [x, x, x]]

     Return value should be "x wins!"

"""
from itertools import chain
from typing import List

import numpy as np


def diagonals(board):
    diagonal_1 = set(board[i][i] for i in range(len(board[0])))
    diagonal_2 = set(board[2 - i][i] for i in range(len(board[0])))
    if len(diagonal_1) == 1:
        return f"wins {board[0][0]}"
    elif len(diagonal_2) == 1:
        return f"wins {board[2][2]}"


def check_rows(board):
    for row in board:
        if len(set(row)) == 1:
            return f"wins {row[0]}"


def tic_tac_toe_checker(board: List[List]) -> str:

    if diagonals(board):
        return diagonals(board)
    else:
        for n in [board, np.transpose(board)]:
            result = check_rows(n)
            if result:
                return result
        return "unfinished" if any("-" in r for r in board) else "draw"


