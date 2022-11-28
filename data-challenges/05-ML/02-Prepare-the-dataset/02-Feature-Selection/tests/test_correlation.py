from nbresult import ChallengeResultTestCase

class TestCorrelation(ChallengeResultTestCase):
    def test_correlated_features(self):
        self.assertEqual(self.result.correlated_features, 0)

