from nbresult import ChallengeResultTestCase
import random


class TestExpectedValueDice(ChallengeResultTestCase):

    def test_expected_value_dice(self):
        expected_value = 3.5
        self.assertEqual(self.result.expected_value, expected_value)
