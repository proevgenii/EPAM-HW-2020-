"""
Write a function that takes a number N as an input and returns N FizzBuzz numbers*
Write a doctest for that function.
Write a detailed instruction how to run doctests**.

That how first steps for the instruction may look like:
 -The simplest way to start using doctest is to end each module M with:
 if __name__ == "__main__":
    import doctest
    doctest.testmod()
 - Than you can run module as : $ python M.py ->  it causes the examples in the docstrings to get executed and verified.
 - But if you want to get a detailed report you must run it with -v: $ python M.py -v.

 - There is also a command line shortcut for running testmod().
  You can instruct the Python interpreter to run the doctest module directly from the standard library
   and pass the module name(s) on the command line:  $ python -m doctest -v example.py
   This will import example.py as a standalone module and run testmod() on it.



Definition of done:
 - function is created
 - function is properly formatted
 - function has doctests
 - instructions how to run doctest with the pytest are provided

You will learn:
 - the most common test task for developers
 - how to write doctests
 - how to run doctests
 - how to write instructions




* https://en.wikipedia.org/wiki/Fizz_buzz
** Энциклопедия профессора Фортрана page 14, 15, "Робот Фортран, чисть картошку!"
"""
from typing import List


def fizzbuzz(n: int) -> List[str]:
    """
    >>> fizzbuzz(5)
    ['1', '2', 'Fizz', '4', 'Buzz']

    """
    result = []
    for i in range(1, (n + 1)):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result
