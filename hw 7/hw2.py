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


def backspace_compare(first: str, second: str):
    s = []
    for c in first:
        if c == "#":
            if s:
                s.pop()
        else:
            s.append(c)

    t = []
    for c in second:
        if c == "#":
            if t:
                t.pop()
        else:
            t.append(c)

    return "".join(s) == "".join(t)


print(backspace_compare("ab#c", "ad#c"))
