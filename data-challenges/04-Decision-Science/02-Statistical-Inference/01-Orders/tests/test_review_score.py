from nbresult import ChallengeResultTestCase


class TestReviewScore(ChallengeResultTestCase):
    def test_review_score(self):
        self.assertEqual(self.result.shape, (99224, 4))
