from nbresult import ChallengeResultTestCase


class TestProducts(ChallengeResultTestCase):
    def test_shape(self):
        self.assertEqual(self.result.shape, (71, 16))
