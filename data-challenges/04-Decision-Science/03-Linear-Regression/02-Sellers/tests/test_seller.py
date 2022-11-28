from nbresult import ChallengeResultTestCase


class TestSeller(ChallengeResultTestCase):
    def test_shape(self):
        self.assertEqual(self.result.shape, (2967, 15))

    def test_median_review_score(self):
        self.assertAlmostEqual(self.result.median, 4.2, 1)
    
