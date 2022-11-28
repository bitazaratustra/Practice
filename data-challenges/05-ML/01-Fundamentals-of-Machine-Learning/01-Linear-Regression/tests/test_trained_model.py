from nbresult import ChallengeResultTestCase


class TestTrainedModel(ChallengeResultTestCase):
    def test_slope(self):
        self.assertAlmostEqual(round(self.result.slope, 3), 0.002, delta=0.001)

    def test_intercept(self):
        self.assertAlmostEqual(round(self.result.intercept, 3), -1.546, delta=0.001)
