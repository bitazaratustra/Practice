from nbresult import ChallengeResultTestCase


class TestPrecision(ChallengeResultTestCase):
    def test_precision(self):
        self.assertGreater(self.result.precision, 0.9)
        self.assertLess(self.result.precision, 0.99)
