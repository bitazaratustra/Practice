from nbresult import ChallengeResultTestCase

class TestLinearSvm(ChallengeResultTestCase):

    def test_score(self):
        # Guesstimated score should be around 0.5
        res = self.result.linear_svm_score
        self.assertGreater(res, 0.2)
        self.assertLess(res, 0.8)
