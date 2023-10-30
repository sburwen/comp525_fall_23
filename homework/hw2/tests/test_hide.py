"""
File: homework/h2/tests/test_hide.py
Contributor: Sean Burwen
Date: 10/26/2023
"""

import unittest
import sys
import os
sys.path.insert(0, os.path.abspath('..'))
from src import linear_efficiency


class TestHide(unittest.TestCase):
    """
    Class to house our tests for hide function
    """
    def test_1(self):
        """
        Test #1 for hide function
        :param: self
        :return: assertion of expected test result
        """
        expected = 'ba**le'
        actual_result = linear_efficiency.hide('babble')
        self.assertEqual(expected, actual_result)
        assert expected == actual_result

    def test_2(self):
        """
        Test #2 for hide function
        :param: self
        :return: assertion of expected test result
        """
        expected = 'tes*ing'
        actual_result = linear_efficiency.hide('testing')
        self.assertEqual(expected, actual_result)
        assert expected == actual_result


if __name__ == "__main__":
    unittest.main()
