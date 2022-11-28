from nbresult import ChallengeResultTestCase


class TestMinimize2d(ChallengeResultTestCase):
    def test_starting_point_shape(self):
        self.assertEqual(self.result.X0_shape, (2,))

    def test_minimum_shape(self):
        self.assertEqual(self.result.minimum_shape, (2,))
