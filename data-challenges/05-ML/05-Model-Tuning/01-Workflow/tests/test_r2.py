from nbresult import ChallengeResultTestCase


class TestR2(ChallengeResultTestCase):
    def test_r2(self):
        self.assertGreater(self.result.r2_test, 0.72)

