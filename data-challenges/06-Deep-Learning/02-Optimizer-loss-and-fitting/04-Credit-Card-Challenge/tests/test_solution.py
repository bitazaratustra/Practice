from nbresult import ChallengeResultTestCase


class TestSolution(ChallengeResultTestCase):
    def test_is_test_set_representative(self):
        """Check if the test set is representative of the real data
        """
        total = self.result.non_fraud_number + self.result.fraud_number
        ratio = self.result.non_fraud_number / self.result.fraud_number
        self.assertGreater(ratio, 200)
        self.assertGreater(total, 30000)
        
    def test_is_score_good_enough(self):
        """Check if the recall result is good enough
        """
        self.assertGreater(self.result.recall, 0.75)
        self.assertGreater(self.result.precision, 0.2)
        
        
        
