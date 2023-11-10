"""
Write a Python function that takes a list of integers as input and returns a 
new list with only the even numbers. For example, if the input is 
[1, 2, 3, 4, 5, 6], the function should return [2, 4, 6].

- Use appropriate function docstrings. 
- Include the time complexity of your function in your docstring.
- No need for design documents, unit tests, etc. Just the function and a call
to the function.

File: midterm/only_evens.py
Contributor: Sean Burwen
Date: 11/9/2023
"""


def only_even(num_list):
    """
    Take list of integers as input and return another list of only its even integers,
    Complexity O(n) (almost)
    :param num_list: list of integers
    :return: list
    """
    new_list = []
    for item in num_list:
        if item % 2 == 0:
            new_list.append(item)
        else:
            pass
    return new_list


print(only_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
