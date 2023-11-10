"""
Create a Python function that reverses a string using a Stack. For example, 
string_reverse("I really love data structures") should return 
"serutcurts atad evol yllaer I".

- Use appropriate function docstrings. 
- Include the time complexity of your function in your docstring.
- No need for design documents, unit tests, etc. Just the function and a call
to the function.

File: midterm/reverse_string.py
Contributor: Sean Burwen
Date: 11/9/2023
"""


def reverse(string):
    """
    Take string as input and returned reverse of it,
    Complexity O(n*2) ??

    :param string: string, input to be reversed
    :return: string, reversed
    """
    stack = []
    new_string = ""
    for char in string:
        stack.append(char)
    for i in range(len(stack)):
        new_string = new_string + stack.pop()
    return new_string


print(reverse("hello"))
