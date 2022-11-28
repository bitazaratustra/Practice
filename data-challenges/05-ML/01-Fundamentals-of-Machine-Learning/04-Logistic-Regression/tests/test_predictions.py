from nbresult import ChallengeResultTestCase
import numpy


class TestPredictions(ChallengeResultTestCase):
    def test_prediction_is_1(self):
        self.assertEqual(self.result.prediction, 1)

    def test_probability(self):
        self.assertGreater(
            self.result.probability, 0.5,
            'Check probability of survival is above 50 percent')

    def test_probability_type(self):
        self.assertIsInstance(
            self.result.probability, numpy.float64,
            'Make sure you stored only one probability')
