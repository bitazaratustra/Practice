from nbresult import ChallengeResultTestCase

class TestSearchComponents(ChallengeResultTestCase):
    def test_best_pc_number(self):
        self.assertGreaterEqual(self.result.best_pc, 100)
        self.assertLessEqual(self.result.best_pc, 300)
