from nbresult import ChallengeResultTestCase

class TestDescent(ChallengeResultTestCase):

    def test_a(self):
        res = self.result.a_100
        self.assertGreater(res, 0.74)
        self.assertLess(res, 0.78)

    def test_b(self):
        res = self.result.b_100
        self.assertGreater(res, 0.006)
        self.assertLess(res, 0.008)

