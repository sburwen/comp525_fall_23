"""
Create a Python function that calculates the factorial of a given non-negative
 integer using recursion. The function should take an integer as input and 
 return its factorial. For example, factorial(5) should return 120.

- Use appropriate function docstrings. 
- Include the time complexity of your function in your docstring.
- No need for design documents, unit tests, etc. Just the function and a call
to the function.


File: midterm/factorial_recursive.py
Contributor: Sean Burwen
Date: 11/9/2023
"""


def factorial(num):
    """
    Takes integer as input and returns its factorial as another integer,
    Complexity O(n)
    :param num: integer
    :return: integer
    """
    if num == 1:
        return 1
    return num * factorial(num-1)


print(factorial(5))
print(factorial(10))
