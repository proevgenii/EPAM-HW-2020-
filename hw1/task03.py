"""
Write down the function, which reads input line-by-line, and find maximum and minimum values.
Function should return a tuple with the max and min values.

For example for [1, 2, 3, 4, 5], function should return [1, 5]

We guarantee, that file exists and contains line-delimited integers.

To read file line-by-line you can use this snippet:

with open("some_file.txt") as fi:
    for line in fi:
        ...

"""
from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    min_max_list = []
    with open(file_name) as fi:
        for line in fi:
            line = [int(i) for i in line.strip("\n").split()]
            min_max_list.append(min(line))
            min_max_list.append(max(line))
            min_max_tup = tuple(min_max_list)
    return min_max_tup
