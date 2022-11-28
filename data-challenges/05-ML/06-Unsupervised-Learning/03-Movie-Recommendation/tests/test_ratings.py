from nbresult import ChallengeResultTestCase


class TestRatings(ChallengeResultTestCase):
    def test_latent_shape(self):
        self.assertEqual(self.result.latent_shape, (9724, 200))
