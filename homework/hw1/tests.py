"""
File: homework/hw1/tests.py
Contributor: Sean Burwen
Date: 10/6/2023
"""
import my_list

test_list1 = [3, 8, 9, 12, 24, 24, 31, 52, 76, 76, 99, 108]
test_list2 = [4, 6, 15, 15, 22, 34, 49, 49, 65, 71]
test_list3 = [0, 1, 2, 3, 4, 5]


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


def extend_test():
    """
    Test inputs for extend() function
    :return: list of integers combined
    """
    # Expected output [3, 8, 9, 12, 24, 24, 31, 52, 76, 76, 99, 108, 4, 6, 15, 15, 22, 34, 49, 49, 65, 71]:
    print(my_list.extend(test_list1, test_list2))

    # Expected output [3, 8, 9, 12, 24, 24, 31, 52, 76, 76, 99, 108, 0, 1, 2, 3, 4, 5]:
    print(my_list.extend(test_list1, test_list3))

    # Expected output [4, 6, 15, 15, 22, 34, 49, 49, 65, 71, 0, 1, 2, 3, 4, 5]:
    print(my_list.extend(test_list2, test_list3))


def remove_test():
    """
    Test inputs for remove() function
    :return: list of integers, with num removed
    """
    # Expected output [4, 6, 15, 15, 22, 34, 65, 71]:
    print(my_list.remove(test_list2, 49))

    # Expected output [6, 15, 15, 22, 34, 49, 49, 65, 71]:
    print(my_list.remove(test_list2, 4))

    # Expected output [4, 6, 15, 15, 22, 34, 49, 49, 65, 71]:
    print(my_list.remove(test_list2, 2))


def index_test():
    """
    Test inputs for index() function
    :return: non-negative integer of the index of the first occurrent of
    `num`
    :return: None, if `num` not found
    """
    # Expected output 8:
    print(my_list.index(test_list1, 76))

    # Expected output 3:
    print(my_list.index(test_list1, 12))

    # Expected output None:
    print(my_list.index(test_list1, 109))


count_test()
extend_test()
remove_test()
index_test()