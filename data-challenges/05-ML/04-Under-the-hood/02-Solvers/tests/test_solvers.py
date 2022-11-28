from nbresult import ChallengeResultTestCase

class TestSolvers(ChallengeResultTestCase):

    def test_fastest_solver(self):
        self.assertIn(self.result.fastest_solver, ['newton-cg', 'lbfgs', 'liblinear'])
