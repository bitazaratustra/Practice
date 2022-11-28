from nbresult import ChallengeResultTestCase


class TestMetadata(ChallengeResultTestCase):
    def test_counter_rows(self):
        self.assertEqual(self.result.counter_shape[0], 9724)

    def test_counter_columns(self):
        self.assertGreater(self.result.counter_shape[1], 1600)

    def test_features_number(self):
        self.assertEqual(self.result.latent_shape[1], 25)
