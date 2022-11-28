from nbresult import ChallengeResultTestCase


class TestBase_precision(ChallengeResultTestCase):
    def test_precision_score(self):
        self.assertTrue(self.result.score < 0.9)
