
from nbresult import ChallengeResultTestCase


class TestUnregularized(ChallengeResultTestCase):
    def test_top_1(self):
        res_set = set(self.result.top_1_feature)
        minimal_truth_set = {"embark_town_Southampton", "embark_town_Queenstown", "embark_town_Cherbourg"}
        self.assertTrue(len(res_set & minimal_truth_set) == 1, "Did you also check for negative coefficients?")
