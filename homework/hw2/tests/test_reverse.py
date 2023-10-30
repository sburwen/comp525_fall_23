"""
File: homework/h2/tests/test_reverse.py
Contributor: Sean Burwen
Date: 10/26/2023
"""

import unittest
import sys
import os
sys.path.insert(0, os.path.abspath('..'))
from src import linear_efficiency


class TestReverse(unittest.TestCase):
    """
    Class to house our tests for reverse function
    """
    def test_1(self):
        """
        Test #1 for reverse function
        :param: self
        :return: assertion of expected test result
        """
        expected = 'olleh'
        actual_result = linear_efficiency.reverse('hello')
        self.assertEqual(expected, actual_result)
        assert expected == actual_result

    def test_2(self):
        """
        Test #2 for reverse function
        :param: self
        :return: assertion of expected test result
        """
        expected = 'gnitset'
        actual_result = linear_efficiency.reverse('testing')
        self.assertEqual(expected, actual_result)
        assert expected == actual_result


if __name__ == "__main__":
    unittest.main()
