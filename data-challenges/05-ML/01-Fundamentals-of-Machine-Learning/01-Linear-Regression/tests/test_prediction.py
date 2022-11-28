from nbresult import ChallengeResultTestCase


class TestPrediction(ChallengeResultTestCase):
    def test_prediction(self):
        self.assertGreater(float(self.result.prediction), 1)
        self.assertLess(float(self.result.prediction), 1.1)
