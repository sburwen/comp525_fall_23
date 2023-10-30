"""
File: homework/h2/tests/test_reduce_adjacent.py
Contributor: Sean Burwen
Date: 10/26/2023
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath('..'))
from src import linear_efficiency


class TestReduceAdjacent(unittest.TestCase):
    """
    Class to house our tests for reduce_adjacent function
    """

    def test_1(self):
        """
        Test #1 for reduce_adjacent function
        :param: self
        :return: assertion of expected test result
        """
        expected = [1, 2, 3, 4, 5]
        actual_result = linear_efficiency.reduce_adjacent([1, 2, 2, 3, 3, 4, 4, 5, 5])
        self.assertEqual(expected, actual_result)
        assert expected == actual_result

    def test_2(self):
        """
        Test #2 for reduce_adjacent function
        :param: self
        :return: assertion of expected test result
        """
        expected = [7, 2, 0, 1, 3]
        actual_result = linear_efficiency.reduce_adjacent([7, 7, 7, 7, 2, 0, 0, 1, 3, 3, 3])
        self.assertEqual(expected, actual_result)
        assert expected == actual_result


if __name__ == "__main__":
    unittest.main()
