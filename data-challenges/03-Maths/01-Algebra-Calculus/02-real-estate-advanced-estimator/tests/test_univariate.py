from nbresult import ChallengeResultTestCase


class TestUnivariate(ChallengeResultTestCase):

    def test_mse(self):
        self.assertLess(self.result.mse_min, 65000)

    def test_best_slope(self):
        self.assertGreater(self.result.slope_best, 0.10)
        self.assertLess(self.result.slope_best, 0.40)

    def test_best_intercept(self):
        self.assertGreater(self.result.intercept_best, -70)
        self.assertLess(self.result.intercept_best, 40)


