from nbresult import ChallengeResultTestCase


class TestRightMerge(ChallengeResultTestCase):
    def test_right_merged_df_shape(self):
        self.assertEqual(self.result.right_merged_shape, (4, 4))

    def test_right_merged_nulls(self):
        self.assertEqual(self.result.right_merged_nulls, 2)
