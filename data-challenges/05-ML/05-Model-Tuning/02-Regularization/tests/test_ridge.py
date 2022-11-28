
from nbresult import ChallengeResultTestCase


class TestRidge(ChallengeResultTestCase):
    def test_top2(self):
        res_set = set(self.result.top_2)
        truth_set = {'sex_female', 'pclass', 'who_child', 'class_Third'}
        self.assertTrue(len(res_set & truth_set) == 2, "Have you regularized enough? Notice that C = 1/alpha")
