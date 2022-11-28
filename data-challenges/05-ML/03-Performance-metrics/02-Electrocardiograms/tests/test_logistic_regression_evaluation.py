from nbresult import ChallengeResultTestCase


class TestLogistic_regression_evaluation(ChallengeResultTestCase):
    def test_accuracy(self):
        self.assertGreater(self.result.accuracy, 0.85)

    def test_recall(self):
        self.assertLess(self.result.recall, 0.4)

    def test_precision(self):
        self.assertLess(self.result.precision, 0.8)
        self.assertGreater(self.result.precision, 0.5)

    def test_f1(self):
        self.assertLess(self.result.f1, 0.6)
        self.assertGreater(self.result.f1, 0.4)
