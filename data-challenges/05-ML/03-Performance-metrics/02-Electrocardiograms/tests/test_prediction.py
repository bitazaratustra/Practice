from nbresult import ChallengeResultTestCase


class TestPrediction(ChallengeResultTestCase):
    def test_prediction_at_risk(self):
        self.assertEqual(self.result.prediction,  "at risk")
