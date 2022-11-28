from nbresult import ChallengeResultTestCase


class TestSolution(ChallengeResultTestCase):
        
    def test_is_score_ok(self):
        self.assertLess(self.result.mae_test, 5)
        
        
