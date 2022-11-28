from nbresult import ChallengeResultTestCase
import random


class TestExpectedValueCoins(ChallengeResultTestCase):

    def test_expected_value_coins(self):
        expected_value_coins = 7
        self.assertEqual(self.result.expected_value_coins, expected_value_coins)
