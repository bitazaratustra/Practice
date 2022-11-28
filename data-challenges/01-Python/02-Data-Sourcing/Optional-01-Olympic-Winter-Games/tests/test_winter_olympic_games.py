# pylint: disable-all

import unittest
import subprocess

from winter_olympic_games import most_decorated_athlete_ever
from winter_olympic_games import country_with_most_gold_medals
from winter_olympic_games import top_three_women_in_five_thousand_meters

class TestWinterOlympicGames(unittest.TestCase):
    def test_most_decorated_athlete_ever(self):
        self.download_files()

        athlete = most_decorated_athlete_ever()
        self.assertEqual(athlete, 'BJOERNDALEN, Ole Einar')

    def test_country_with_most_gold_medals_between_2002_and_2014(self):
        self.download_files()

        country = country_with_most_gold_medals(2002, 2014)
        self.assertEqual(country, 'Canada')

    def test_country_with_most_gold_medals_between_1994_and_1998(self):
        self.download_files()

        country = country_with_most_gold_medals(1994, 1998)
        self.assertEqual(country, 'Germany')

    def test_top_three_women_in_five_thousand_meters(self):
        self.download_files()

        women = top_three_women_in_five_thousand_meters()
        self.assertEqual(women, ['PECHSTEIN, Claudia', 'NIEMANN-STIRNEMANN, Gunda', 'HUGHES, Clara'])

    # HELPER METHODS
    def download_files(self):
        # Download the necessary files for testing
        subprocess.call([
            "curl", "https://wagon-public-datasets.s3.amazonaws.com/01-Python/02-Data-Sourcing/olympics_dictionary.csv",
            "--output", "data/dictionary.csv"
        ])

        subprocess.call([
            "curl", "https://wagon-public-datasets.s3.amazonaws.com/01-Python/02-Data-Sourcing/olympics_winter.csv",
            "--output", "data/winter.csv"
        ])
