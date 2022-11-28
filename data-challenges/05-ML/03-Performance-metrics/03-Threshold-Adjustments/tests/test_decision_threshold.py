from nbresult import ChallengeResultTestCase


class TestDecision_threshold(ChallengeResultTestCase):
    def test_new_threshold(self):
        self.assertLess(self.result.threshold, 0.9)
        self.assertGreater(self.result.threshold, 0.8)
