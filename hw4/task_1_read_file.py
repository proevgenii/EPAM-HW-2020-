"""
Write a function that gets file path as an argument.
Read the first line of the file.
If first line is a number return true if number in an interval [1, 3)*
and false otherwise.
In case of any error, a ValueError should be thrown.

Write a test for that function using pytest library.

Definition of done:
 - function is created
 - function is properly formatted
 - function has positive and negative tests
 - all temporary files are removed after test run

You will learn:
 - how to test Exceptional cases
 - how to clean up after tests
 - how to check if file exists**
 - how to handle*** and raise**** exceptions in test. Use sample from the documentation.

* https://en.wikipedia.org/wiki/Interval_(mathematics)#Terminology
** https://docs.python.org/3/library/os.path.html
*** https://docs.python.org/3/tutorial/errors.html#handling-exceptions
**** https://docs.python.org/3/tutorial/errors.html#raising-exceptions
"""

file = open("test.txt", "w")
file.write("1 2 3\n2\n3")
file.close()


def read_magic_number(path: str) -> bool:
    try:
        with open(path, "r") as fi:
            try:
                first_line = float(fi.readline())
                if 1 < first_line <= 3:
                    return True
                else:
                    return False
            except ValueError:
                raise ValueError(
                    f"Invalid data in firs line of '{path}', not a number "
                )

    except IOError:
        raise IOError("File not accessible")
