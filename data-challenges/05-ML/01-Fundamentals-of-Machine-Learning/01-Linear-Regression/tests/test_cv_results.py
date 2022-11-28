from nbresult import ChallengeResultTestCase


class TestCvResults(ChallengeResultTestCase):
    def test_cv_results(self):
        self.assertEqual(len(self.result.cv_result['test_score']), 5)

    def test_cv_mean(self):
        self.assertLess(self.result.mean_score, 0.6)
        self.assertGreater(self.result.mean_score, 0.5)

