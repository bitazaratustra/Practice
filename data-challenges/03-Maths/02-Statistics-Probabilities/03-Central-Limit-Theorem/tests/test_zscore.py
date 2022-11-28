from nbresult import ChallengeResultTestCase


class TestZscore(ChallengeResultTestCase):
    def test_z_score_value(self):
        self.assertGreater(
            self.result.z, 3.6,
            'The zscore should be more than 3.6'
        )
        self.assertGreater(
            3.7,
            self.result.z,
            'The zscore should be less than 3.7'
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
