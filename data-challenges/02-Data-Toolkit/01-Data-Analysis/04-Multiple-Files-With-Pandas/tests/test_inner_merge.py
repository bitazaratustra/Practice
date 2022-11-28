from nbresult import ChallengeResultTestCase


class TestInnerMerge(ChallengeResultTestCase):
    def test_inner_merged_shape(self):
        self.assertEqual(self.result.inner_merged_shape, (3, 4))

    def test_inner_merged_nulls(self):
        self.assertEqual(self.result.inner_merged_nulls, 0)
