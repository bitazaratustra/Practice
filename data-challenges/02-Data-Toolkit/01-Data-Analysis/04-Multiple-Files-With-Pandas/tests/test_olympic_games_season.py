from nbresult import ChallengeResultTestCase


class TestOlympicGamesSeason(ChallengeResultTestCase):
    def test_top_10_countries_shape(self):
        self.assertEqual(self.result.top_country_season_shape, (10, 3))

    def test_top_10_countries_summer(self):
        self.assertEqual(self.result.top_country_1_summer, 2087)

    def test_top_10_countries_winter(self):
        self.assertEqual(self.result.top_country_10_winter, 87)
