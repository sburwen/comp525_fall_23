"""
Parser for Ramen Stats
Jon
20211210
"""


class RamenStats:
    """
    Ramen stats provide interface for reading and parsing ramen stats
    """

    file_name = 'ramen.csv'

    def __init__(self):
        """
        Constructor
        """
        self.ramen_set = []
        with open(self.file_name, 'r', encoding='UTF-8') as fin:
            lines = fin.readlines()[1:]
            for lin in lines:
                lin = lin.strip()
                lin = lin.split(",")
                lin[5] = float(lin[5])
                self.ramen_set.append(lin)

    def get_average_for_all(self):
        """
        Returns the average ramen rating across ALL ratings
        :return: the average for ratings for the given country
        :rtype: float
        """
        total_rating = 0
        for line in self.ramen_set:
            total_rating += line[5]
        return total_rating / len(self.ramen_set)

    def get_average_for_country(self, country):
        """
        Returns the average ramen rating for a given country
        :param country: the country for which the ratings belong to
        :type country: string
        :return: the average for ratings for the given country
        :rtype: float
        """
        total_rating = 0
        found_ratings = 0
        for line in self.ramen_set:
            if line[4] == country:
                total_rating += line[5]
                found_ratings += 1
        return total_rating / found_ratings

    def get_percent_of_variety_that_include_the_word_ramen(self):
        """
        Returns the percentage of ramen variety that include the word "ramen"
        :return: the percentage of ramen variety that include the word "ramen"
        :rtype: float
        """
        found_ratings = 0
        for line in self.ramen_set:
            if "Ramen" in line[2]:
                found_ratings += 1
        return found_ratings / len(self.ramen_set)

    def get_ramen_by_country(self):
        """
        Returns a dictionary with the ramen categorized by country
        :return:  dict with keys being the country name and values being
            a list of ramen for that country
            ex: {'USA': [[2580, 'New Touch', "T's Restaurant', 'Cup', 'etc]]
        :rtype: dictionary
        """
        data = {}
        for line in self.ramen_set:
            if line[4] not in data:
                data[line[4]] = []
            data[line[4]].append(line)
        return data


if __name__ == "__main__":
    stats = RamenStats()

    # average all expected to be ???
    print(f"Average All: {stats.get_average_for_all():.2f}")

    # average USA expected to be ???
    print(f"Average USA: {stats.get_average_for_country('USA'):.2f}")
    # Num ramen with "ramen" in their variety expected to be ???
    percent_ramen = stats.get_percent_of_variety_that_include_the_word_ramen()
    print(f"Variety % ramen: {percent_ramen:.2f}")
    #
    # Num ramen for Japan expected to be ???
    ramen_categorized = stats.get_ramen_by_country()
    print(f"Num ramen for Japan: {len(ramen_categorized['Japan'])}")
