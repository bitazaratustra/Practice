from nbresult import ChallengeResultTestCase


class TestLeftMerge(ChallengeResultTestCase):
    def test_left_merged_df_shape(self):
        self.assertEqual(self.result.left_merged_shape, (4, 4))

    def test_left_merged_nulls(self):
        self.assertEqual(self.result.left_merged_nulls, 1)
