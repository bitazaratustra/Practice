from nbresult import ChallengeResultTestCase


class TestFeatureEngineering(ChallengeResultTestCase):
    def test_unicity_of_movies(self):
        self.assertFalse(self.result.unique_movies,
                         'Make sure you have only one row per movie')

    def test_metadata_has_tags(self):
        self.assertIn('serial killer',
                      self.result.metadata['metadata'].values[0])

    def test_metadata_has_genres(self):
        self.assertIn('Crime Drama Horror Mystery Thriller',
                      self.result.metadata['metadata'].values[0])

    def test_merged_df_rows(self):
        self.assertEqual(self.result.merged_df_rows, 9724)
