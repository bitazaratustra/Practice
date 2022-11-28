from nbresult import ChallengeResultTestCase


class TestProjection(ChallengeResultTestCase):
    def test_shape(self):
        self.assertEqual(self.result.shape[1], 150)
