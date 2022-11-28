from nbresult import ChallengeResultTestCase

class TestScaled_features(ChallengeResultTestCase):
    def test_scaled_features(self):
        min = self.result.scaled_features.min()
        self.assertEqual((min < 10).all(), True)
        self.assertEqual((min > -10).all(), True)
