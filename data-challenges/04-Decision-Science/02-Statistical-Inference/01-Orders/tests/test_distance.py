from nbresult import ChallengeResultTestCase


class TestDistance(ChallengeResultTestCase):
    def test_distance(self):
        self.assertGreater(self.result.mean, 580)
        self.assertLess(self.result.mean, 620)
