from nbresult import ChallengeResultTestCase


class TestPolySvm(ChallengeResultTestCase):

    def test_performance(self):
        res = self.result.poly_svm_performance
        truth = [
            "captures all reducible error",
            "has only irreducible errors left",
        ]
        self.assertCountEqual(res, truth)
