from nbresult import ChallengeResultTestCase
from math import sqrt


class TestProbability(ChallengeResultTestCase):
    def test_mu_expected_is_mu(self):
        self.assertEqual(self.result.mu_expected, self.result.mu)

    def test_sigma_expected_value(self):
        self.assertEqual(
            self.result.sigma_expected,
            self.result.sigma/sqrt(self.result.n)
        )

    def test_probability_is_very_low(self):
        self.assertGreater(
            0.001,
            self.result.proba,
            'The probability should be less than 0.1%.'
        )

    def test_probability_is_valid(self):
        self.assertGreater(
            0.99,
            self.result.proba,
            '''The probability is way too high. Check what the
`scipy.stats.norm.cdf()` method returns.'''
        )
