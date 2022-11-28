from nbresult import ChallengeResultTestCase


class TestSolution(ChallengeResultTestCase):
    def test_cv_results(self):
        search = self.result.search
        self.assertEqual(search.scoring, "precision")
        self.assertGreaterEqual(search.cv, 2)
        self.assertGreaterEqual(len(search.cv_results_["mean_test_score"]), 5)
