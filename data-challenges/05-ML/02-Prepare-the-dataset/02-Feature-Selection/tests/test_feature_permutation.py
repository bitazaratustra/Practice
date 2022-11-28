from nbresult import ChallengeResultTestCase

class TestFeature_permutation(ChallengeResultTestCase):
    def test_best_feature(self):
        self.assertEqual(self.result.feature, 'GrLivArea')

