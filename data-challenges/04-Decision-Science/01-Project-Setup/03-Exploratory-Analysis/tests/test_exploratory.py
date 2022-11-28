from nbresult import ChallengeResultTestCase

class TestExploratory(ChallengeResultTestCase):

    def test_n_missing_reviews(self):
        self.assertEqual(self.result.n, 768)