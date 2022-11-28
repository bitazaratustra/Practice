from nbresult import ChallengeResultTestCase


class TestFlats(ChallengeResultTestCase):
    def test_shape(self):
        self.assertEqual(self.result.shape, (1000, 4))

    def test_columns(self):
        self.assertEqual(
            list(self.result.columns),
            ['price', 'bedrooms', 'surface', 'floors']
        )
