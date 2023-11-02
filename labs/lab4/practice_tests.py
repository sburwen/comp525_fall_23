"""
test_parse_season.py
Sean Burwen
Updated 11/2/23
"""

import unittest
from practice_dictionaries import Practice


class TestParseSeasons(unittest.TestCase):
    """
    Tests for parse_seasons() method
    """
    def setUp(self):
        """
        Define attribute p to hold object of type Problems
        """
        self.p = Practice()

    def test_brief_descriptions(self):
        """
        Test case with short season descriptions
        """
        input1 = {
            'spring': 'warm',
            'summer': 'hot',
            'fall': 'justright',
            'winter': 'cold'
        }
        actual_result = self.p.parse_seasons(input1)
        expected_result = 'springwarmsummerhotfalljustrightwintercold'
        self.assertEqual(actual_result, expected_result)

    def test_inventory_add(self):
        """
        test case for update inventory
        """
        input1 = {
            'milk': 37,
            'eggs': 26,
            'bread': 15,
            'cheese': 12
        }
        actual_result = self.p.update_inventory(input1, 10)
        expected_result = {
            'milk': 47,
            'eggs': 36,
            'bread': 25,
            'cheese': 22
        }
        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
