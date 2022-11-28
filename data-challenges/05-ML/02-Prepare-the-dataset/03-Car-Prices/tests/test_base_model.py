from nbresult import ChallengeResultTestCase

class TestBase_model(ChallengeResultTestCase):
    def test_base_model_score(self):
        self.assertEqual(self.result.score > 0.8, True)
