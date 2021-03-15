"""
Write a function that will receive a string and write it to stderr
if line starts with "error" and to the stdout otherwise.


>>> my_precious_logger("error: file not found")
# stderr
'error: file not found'


>>> my_precious_logger("OK")
# stdout
'OK'

Definition of done:
 - function is created
 - function is properly formatted
 - function has positive tests

You will learn:
 - how to write to stderr
 - how to test output to the stderr and stdout


"""
import re
import sys


def my_precious_logger(text: str):
    result = re.findall(r"^\w+", text)  # get only first word
    if result == ["error"]:
        return print(text, file=sys.stderr)
    else:
        return print(text, file=sys.stdout)
