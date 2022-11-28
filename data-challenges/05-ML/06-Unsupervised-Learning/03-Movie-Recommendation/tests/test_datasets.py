from nbresult import ChallengeResultTestCase
import numpy as np


class TestDatasets(ChallengeResultTestCase):
    def test_movies_shape(self):
        self.assertEqual(
            self.result.movies_shape, (9724, 3),
            'Make sure you kept only the movies that have been rated')

    def test_tags_shape(self):
        self.assertEqual(self.result.tags_shape, (3683, 4))

    def test_ratings_shape(self):
        self.assertEqual(self.result.ratings_shape, (100836, 4))

    def test_genres_are_cleaned(self):
        self.assertFalse(np.all(self.result.genres_cleaned),
                         'Make sure you removed all `|` from `genres`')
