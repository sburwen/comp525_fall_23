"""
practice_dictionaries.py
Sean Burwen
Updated 11/2/2023
"""


class Practice(object):
    """
    Illustrate methods that transform an input dictionary into some output
    """

    def parse_seasons(self, season_dict):
        """
        Create a string with info from season_dict
        season_dict: dictionary
            keys: strings - season names
            values: strings - season descriptions
        Returns: string with season names and descriptions and no spaces or
            other characters in between
        """
        ugly_string = ""
        for season, desc in season_dict.items():
            ugly_string = ugly_string + season + desc
        ugly_string = ugly_string.replace(" ", "")
        return ugly_string

    def update_inventory(self, inventory_dict, quantity_added):
        """
        Returns new dictionary with quanties for each itmem in inventory_dict
            increased by quantity-added
        inventory_dict: dictionary
            keys: strings - inventory item names
            values: int - inventory quantity of item
        Returns: dictionry
        """
        new_dict = {}
        for item in inventory_dict.keys():
            current = inventory_dict[item]
            new_dict[item] = current + quantity_added
        return new_dict


if __name__ == '__main__':
    p = Practice()
    input1 = {
        'spring': 'warm',
        'summer': 'hot',
        'fall': 'just right',
        'winter': 'cold'
    }
    result = p.parse_seasons(input1)
    print(f'parse_seasons({input1}) returns {result}')
