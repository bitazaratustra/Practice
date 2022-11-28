
from nbresult import ChallengeResultTestCase


class TestLasso(ChallengeResultTestCase):
    def test_zero_impact(self):
        res_set = set(self.result.zero_impact_features)
        minimal_truth_set = {"embark_town_Queenstown"}
        self.assertTrue(len(res_set & minimal_truth_set) == 1, "Have you regularized enough?")
