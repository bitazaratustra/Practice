from nbresult import ChallengeResultTestCase


class TestRecommendation(ChallengeResultTestCase):
    def test_recommendation(self):
        self.assertEqual(self.result.recommendation, "recommend")
