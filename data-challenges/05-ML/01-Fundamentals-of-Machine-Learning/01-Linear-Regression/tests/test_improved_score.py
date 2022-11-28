from nbresult import ChallengeResultTestCase


class TestImprovedScore(ChallengeResultTestCase):
    def test_improved_score(self):
        self.assertGreater(self.result.improved_score, 0.6, "Did you pick the right feature?")
