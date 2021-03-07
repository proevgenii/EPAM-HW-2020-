"""
    Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
import string
from typing import List


def get_longest_diverse_words(file_path: str) -> List[str]:
    with open(file_path) as fi:
        words_longest = sorted([word for line in fi for word in line.split()], key =len , reverse=True)
        words_uniq = sorted(words_longest, key=set, reverse=True)[0:11:1]
    return words_uniq


def get_rarest_char(file_path: str) -> str:
    char_dict={}
    with open(file_path) as fi:
        for char in fi.read().strip('\n').strip():
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return sorted(char_dict.items(),key = lambda items: items[1])[0][0]


def count_punctuation_chars(file_path: str) -> int:
    punc = set('''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~''')
    with open(file_path) as fi:
        file_text =  fi.read()
    chars_punc = sum(char in punc for char in file_text)
    return chars_punc


def count_non_ascii_chars(file_path: str) -> int:
    ascii = set("""!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~""")
    with open(file_path) as fi:
        file_text =  fi.read()
    non_ascii_char=sum(char not in ascii for char in file_text)
    return non_ascii_char


def get_most_common_non_ascii_char(file_path: str) -> str:
    non_ascii = {}
    with open(file_path) as fi:
        file_text = fi.read()
        for char in file_text:
            if 0 <= ord(char) <= 127:
                continue
            elif char in non_ascii:
                non_ascii[char] +=1
            elif char not in non_ascii:
                non_ascii[char] = 1
    return sorted(non_ascii.items(),key = lambda items: items[1], reverse=True)[0][0]




get_most_common_non_ascii_char(r'\University\EPAM\hw2\file.txt')