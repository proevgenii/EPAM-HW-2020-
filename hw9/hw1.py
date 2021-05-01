"""
Write a function that merges integer from sorted files and returns an iterator

file1.txt:
1
3
5

file2.txt:
2
4
6


>>> list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]
"""
from contextlib import ExitStack
from itertools import cycle, islice
from pathlib import Path
from typing import Iterator, List, Union


def merge_sorted_files(*iters):
    num_active = len(iters)
    nexts = cycle(iter(it).__next__ for it in iters)
    while num_active:
        try:
            for next in nexts:
                yield int(next().strip("\n"))
        except StopIteration:
            # Remove the iterator we just exhausted from the cycle.
            num_active -= 1
            nexts = cycle(islice(nexts, num_active))


def opener(file_list: [Path, str]) -> Iterator:
    with ExitStack() as stack:
        files = [stack.enter_context(open(name)) for name in file_list]
        yield from merge_sorted_files(*files)
