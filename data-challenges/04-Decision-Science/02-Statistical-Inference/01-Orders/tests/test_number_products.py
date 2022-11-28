from nbresult import ChallengeResultTestCase


class TestNumberProducts(ChallengeResultTestCase):
    def test_review_score(self):
        self.assertEqual(self.result.shape, (98666, 2))
