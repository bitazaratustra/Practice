from nbresult import ChallengeResultTestCase


class TestOlympicGames(ChallengeResultTestCase):
    def test_top_10_countries_medals(self):
        self.assertEqual(self.result.top_country_1, 2472)
        self.assertEqual(self.result.top_country_10, 563)
