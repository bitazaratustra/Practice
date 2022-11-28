from nbresult import ChallengeResultTestCase


class TestDistribution(ChallengeResultTestCase):

    def test_skewness_is_right(self):
        self.assertEqual(self.result.skewness, 'right')

    def test_mean_is_a_float(self):
        self.assertIsInstance(self.result.mu, float)

    def test_standard_deviation_is_a_float(self):
        self.assertIsInstance(self.result.sigma, float)

    def test_mean_value(self):
        self.assertGreater(self.result.mu, 2.99)
        self.assertGreater(3, self.result.mu)

    def test_standard_deviation_value(self):
        self.assertGreater(self.result.sigma, 1.38)
        self.assertGreater(1.39, self.result.sigma)
