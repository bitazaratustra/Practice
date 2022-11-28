from nbresult import ChallengeResultTestCase

class TestBaseline(ChallengeResultTestCase):

    def test_accuracy(self):
        self.assertAlmostEqual(self.result.accuracy, 1/7, places=2)
