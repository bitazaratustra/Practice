from nbresult import ChallengeResultTestCase

class TestDeeperModel(ChallengeResultTestCase):

    def test_accuracy(self):
        self.assertGreater(self.result.accuracy, 0.90)
from nbresult import ChallengeResultTestCase
