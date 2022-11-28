from nbresult import ChallengeResultTestCase

class TestStrong_model(ChallengeResultTestCase):
    def test_strong_model_score(self):
        self.assertEqual(self.result.score > 0.86, True)
