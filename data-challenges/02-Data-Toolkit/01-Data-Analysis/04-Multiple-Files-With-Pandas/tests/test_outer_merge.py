from nbresult import ChallengeResultTestCase


class TestOuterMerge(ChallengeResultTestCase):
    def test_outer_merged_df_shape(self):
        self.assertEqual(self.result.outer_merged_shape, (5, 4))

    def test_outer_merged_nulls(self):
        self.assertEqual(self.result.outer_merged_nulls, 3)
