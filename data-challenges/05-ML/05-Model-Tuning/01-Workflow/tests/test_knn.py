from nbresult import ChallengeResultTestCase


class TestKnn(ChallengeResultTestCase):
    def test_best_k(self):
        self.assertGreaterEqual(self.result.best_k, 10)
        self.assertLessEqual(self.result.best_k, 25)

    def test_best_score(self):
        self.assertGreater(self.result.best_score, 0.76)
