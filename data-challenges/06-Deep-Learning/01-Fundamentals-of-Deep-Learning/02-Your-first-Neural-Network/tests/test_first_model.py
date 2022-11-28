from nbresult import ChallengeResultTestCase

class TestFirstModel(ChallengeResultTestCase):

    def test_accuracy(self):
        self.assertGreater(self.result.accuracy, 0.80)
