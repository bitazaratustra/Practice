from nbresult import ChallengeResultTestCase

class TestGeneralization(ChallengeResultTestCase):

    def test_number_misclassified(self):
        res = self.result.number_misclassified_test
        self.assertGreaterEqual(res, 0)
        self.assertLess(res, 10)
