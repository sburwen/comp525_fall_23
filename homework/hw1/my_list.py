"""
File: homework/hw1/my_list.py
Initial contributor: Mihaela
Contributor: Sean Burwen
Date: 10/6/2023

Implementation requirement:
- Do not call built-in list methods, except for append()
"""


def count(num_list, num):
    """
    Find how many times `num` is in `num_list`.
    :param num_list: list of integers
    :param num: integer
    :return: integer, representing how many times `num` is in `num_list`
    """
    counter = 0
    for i in num_list:
        if i == num:
            counter += 1
    return counter


def extend(num_list, another_num_list):
    """
    Build and return a new list that has the items in `num_list` followed by
    the itmes in `another_num_list` preserving the order.
    :param num_list: list of integers
    :param another_num_list: list of integers
    :return: list of integers
    """
    new_list = num_list[:]
    for i in another_num_list:
        new_list.append(i)
    return new_list


def remove(num_list, num):
    """
    Build and return a new list that has the items in `num_list` in their
    original order, except for `num` item, which gets removed.
    :param num_list: list of integers
    :param num: integer
    :return: list of integers
    """
    new_list = []
    for i in num_list:
        if i != num:
            new_list.append(i)
    return new_list


def index(num_list, num):
    """
    Find index of `num` in `num_list`.
    :param num_list: list of integers
    :param num: integer
    :return: non-negative integer of the index of the first occurrent of
    `num`
    :return: None, if `num` not found
    """
    counter = 0
    flag = 0
    for i in num_list:
        if i == num:
            flag = 1
            break
        else:
            counter += 1
    if flag == 0:
        counter = None
    return counter
