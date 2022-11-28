from nbresult import ChallengeResultTestCase

class TestReduced_complexity_model(ChallengeResultTestCase):
    def test_reduced_complexity_score(self):
        self.assertEqual(self.result.model_score >= 0.6, True)

