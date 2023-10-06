"""
File: homework/hw1/tests.py
Contributor: Sean Burwen
Date: 10/6/2023
"""
import my_list

test_list1 = [3, 8, 9, 12, 24, 24, 31, 52, 76, 76, 99, 108]
test_list2 = [4, 6, 15, 15, 22, 34, 49, 49, 65, 71]


def count_test():
    """
    Test inputs for count() function
    :return: integer, representing how many times `num` is in `num_list`
    """
    # Expected output 1:
    print(my_list.count(test_list1, 9))

    # Expected output 2:
    print(my_list.count(test_list1, 24))

    # Expected output 0:
    print(my_list.count(test_list1, 1))
