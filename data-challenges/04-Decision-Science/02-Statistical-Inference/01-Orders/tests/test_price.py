from nbresult import ChallengeResultTestCase


class TestPrice(ChallengeResultTestCase):
    def test_price(self):
        self.assertEqual(self.result.shape, (98666,3))
