# pylint: disable=missing-docstring

import csv

COUNTRIES_FILEPATH = "data/dictionary.csv"
MEDALS_FILEPATH = "data/winter.csv"


def most_decorated_athlete_ever():
    """Returns who won the most winter olympic games medals (gold/silver/bronze) ever"""
    with open(MEDALS_FILEPATH, newline='') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        athletes = [row[4] for row in data]

        winner = {}
        for athlete in athletes:
            if athlete in winner:
                winner[athlete] += 1
            else:
                winner[athlete] = 1
        most_decorated_athlete = max(winner, key=winner.get)
        return most_decorated_athlete





def country_with_most_gold_medals(min_year, max_year):
    """Returns which country won the most gold medals between `min_year` and `max_year`"""
    pass  # YOUR CODE HERE

def top_three_women_in_five_thousand_meters():
    """Returns the three women with the most 5000 meters medals(gold/silver/bronze)"""
    pass  # YOUR CODE HERE


most_decorated_athlete_ever()
