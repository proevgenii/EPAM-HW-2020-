"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".

    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".

    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".

"""


def clear_string(string: str):
    clear = []
    for char in string:
        if char == "#":
            if clear:
                clear.pop()
        else:
            clear.append(char)

    return "".join(clear)


def backspace_compare(first_str: str, second_str: str):
    return clear_string(first_str) == clear_string(second_str)
