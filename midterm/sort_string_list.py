"""
Write a Python function that takes a list of strings and sorts them based on 
the length of the strings, with the shortest strings coming first. 
For example, if the input is ["apple", "banana", "cherry", "date"], the 
function should return ["date", "apple", "cherry", "banana"].

- Use appropriate function docstrings. 
- Include the time complexity of your function in your docstring.
- No need for design documents, unit tests, etc. Just the function and a call
to the function.

File: midterm/sort_string_list.py
Contributor: Sean Burwen
Date: 11/9/2023
"""


def sort(input_list):
    """
    This is a bubble sort, and it's slow :(. Takes input list and sorts by length of items,
    Complexity O(n^2)

    :param input_list: list of strings
    :return: list of strings sorted by length
    """
    for i in range(len(input_list) - 1, 0, -1):
        for j in range(i):
            if len(input_list[j]) > len(input_list[j + 1]):
                temp = input_list[j]
                input_list[j] = input_list[j + 1]
                input_list[j + 1] = temp
    return input_list


test_list = ["goodbye", "hello", "1", "up", "down", "cat", "dog", "bird", ""]
print(sort(test_list))
