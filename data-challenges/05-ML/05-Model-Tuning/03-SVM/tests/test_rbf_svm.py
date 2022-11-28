from nbresult import ChallengeResultTestCase


class TestRbfSvm(ChallengeResultTestCase):

    def test_hyperparams(self):

        self.assertGreaterEqual(self.result.best_gamma, 0.1)
        self.assertLess(self.result.best_gamma, 5)

        self.assertGreaterEqual(self.result.best_c, 1)
        self.assertLess(self.result.best_c, 1000)

