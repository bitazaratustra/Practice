from nbresult import ChallengeResultTestCase


class TestRecommender(ChallengeResultTestCase):
    def test_best_similarity(self):
        self.assertEqual(
            self.result.best_similarity,
            'hybrid',
            'Which similarity gives Toy Story 2 the closer to the first opus?')
