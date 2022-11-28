from nbresult import ChallengeResultTestCase


class TestReduced_accuracy(ChallengeResultTestCase):
    def test_accuracy(self):
        self.assertGreater(self.result.accuracy, 0.6)
