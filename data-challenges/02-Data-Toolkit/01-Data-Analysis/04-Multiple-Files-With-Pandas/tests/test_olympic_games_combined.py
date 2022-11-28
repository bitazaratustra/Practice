from nbresult import ChallengeResultTestCase
import numpy as np


class TestOlympicGamesCombined(ChallengeResultTestCase):
    def test_top_10_combined_shape(self):
        self.assertEqual(self.result.top_combined_shape, (11, 2))

    def test_combined_1(self):
        self.assertEqual(self.result.top_combined_1_event, 1078)
        self.assertEqual(self.result.top_combined_1_medal, 2472)

    def test_combined_10(self):
        self.assertIsInstance(self.result.top_combined_10_event, type(np.nan))
        self.assertEqual(self.result.top_combined_10_medal, 563)
