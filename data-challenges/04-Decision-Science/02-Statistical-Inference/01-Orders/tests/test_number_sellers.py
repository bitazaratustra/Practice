from nbresult import ChallengeResultTestCase


class TestNumberSellers(ChallengeResultTestCase):
    def test_number_seller(self):
        self.assertEqual(self.result.shape, (98666,2))
