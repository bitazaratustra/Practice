from nbresult import ChallengeResultTestCase


class TestSolution(ChallengeResultTestCase):
    def test_solution(self):
        self.assertEqual(list(self.result.predicted_class)[0], 0)
