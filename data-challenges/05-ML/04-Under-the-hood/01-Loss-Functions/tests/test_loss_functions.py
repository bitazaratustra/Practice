from nbresult import ChallengeResultTestCase

class TestLossFunctions(ChallengeResultTestCase):

    def test_r2(self):
        self.assertGreater(self.result.r2, 0.7)

    def test_r2_mae(self):
        self.assertGreater(self.result.r2_mae, 0.7)

    def test_max_error_order(self):
        self.assertLess(abs(self.result.max_error), abs(self.result.max_error_mae))
