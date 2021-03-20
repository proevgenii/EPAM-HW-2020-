"""
    Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
import re
import string
from typing import List


def get_longest_diverse_words(file_path: str) -> List[str]:
    with open(file_path, encoding="unicode-escape", errors="replace") as fi:
        words_longest = sorted(
            [
                word
                for line in fi
                for word in re.findall(r"\w+", line.replace("-", "").replace("'", ""))
            ],
            key=len,
            reverse=True,
        )
        words_uniq = sorted(words_longest, key=set, reverse=True)[0:11:1]

    return words_uniq


def get_rarest_char(file_path: str) -> str:
    """
    >>> get_rarest_char('file.txt')
    g
    >>> get_rarest_char('data.txt')
    Y
    """

    char_dict = {}
    with open(file_path, encoding="unicode-escape", errors="replace") as fi:
        for char in fi.read().strip():
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return sorted(char_dict.items(), key=lambda items: items[1])[0][0]


def count_punctuation_chars(file_path: str) -> int:
    """
    >>> count_punctuation_chars('file.txt')
    0
    >>> count_punctuation_chars('data.txt')
    8277
    """
    with open(file_path, encoding="unicode-escape", errors="replace") as fi:
        file_text = fi.read()
    chars_punc = sum(char in string.punctuation for char in file_text)
    return chars_punc


def count_non_ascii_chars(file_path: str) -> int:
    """
    >>> count_non_ascii_chars('file.txt')
    16
    >>> count_non_ascii_chars('data.txt')
    0
    """
    with open(file_path, encoding="utf-8") as fi:
        file_text = fi.read()
    non_ascii_char = sum(char.isascii() is False for char in file_text)
    return non_ascii_char


def get_most_common_non_ascii_char(file_path: str) -> str:
    """
    >>> get_most_common_non_ascii_char('file.txt')
    'ü'
    """
    non_ascii = {}
    with open(file_path, encoding="utf-8") as fi:
        for line in fi:
            chars = re.findall(r"\w", line)
            for char in chars:
                if not char.isascii() and char in non_ascii:
                    non_ascii[char] += 1
                elif not char.isascii() and char not in non_ascii:
                    non_ascii[char] = 1

    return (
        sorted(non_ascii.items(), key=lambda items: items[1], reverse=True)[0][0]
        if len(non_ascii) > 0
        else None
    )
