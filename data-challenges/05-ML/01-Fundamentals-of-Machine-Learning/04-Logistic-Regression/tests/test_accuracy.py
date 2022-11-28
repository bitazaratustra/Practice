from nbresult import ChallengeResultTestCase


class TestAccuracy(ChallengeResultTestCase):
    def test_accuracy(self):
        self.assertGreater(self.result.accuracy, 0.6)
