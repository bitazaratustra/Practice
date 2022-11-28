from nbresult import ChallengeResultTestCase

class TestNewDataPrediction(ChallengeResultTestCase):

    def test_predicted_class(self):
        self.assertEqual(self.result.predicted_class, 0)

    def test_predicted_proba(self):
        self.assertGreater(self.result.predicted_proba_of_class,0.93)
        self.assertLess(self.result.predicted_proba_of_class, 0.999, "Did you remember to normalise the new wine data?")

