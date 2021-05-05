"""
Write a function that takes directory path, a file extension and an optional tokenizer.
It will count lines in all files with that extension if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.

For dir with two files from hw1.py:
>>> universal_file_counter(test_dir, "txt")
6
>>> universal_file_counter(test_dir, "txt", str.split)
6

"""
import os
from pathlib import Path
from typing import Callable, Optional


def universal_file_counter(
    dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None
) -> int:
    result = 0
    files_list = []
    for file in os.listdir(dir_path):
        if file.endswith(file_extension):
            files_list.append(file)
            with open(file) as fi:

                if not tokenizer:
                    result += len(list(fi))

                else:
                    text = fi.read()
                    result = list(map(tokenizer, text))[-1][0]

    return result
