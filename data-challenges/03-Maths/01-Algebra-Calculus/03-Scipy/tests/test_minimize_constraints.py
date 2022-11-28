from nbresult import ChallengeResultTestCase
import numpy as np


class TestMinimizeConstraints(ChallengeResultTestCase):
    def test_starting_point_shape(self):
        self.assertEqual(
            self.result.X0.shape,
            (4,),
            'X0 should be a (4,) ndarray'
        )

    def test_bounds_values(self):
        for bound in self.result.bounds:
            self.assertEqual(
                bound,
                (1, 5),
                'Boundaries should be between 1 and 5'
            )

    def test_minimum_shape(self):
        self.assertEqual(
            self.result.Xmin.shape,
            (4,),
            'The local minimum should be a (4,) ndarray'
        )

    def test_first_constraint(self):
        first_constraint = np.sum(self.result.Xmin ** 2)
        self.assertGreater(first_constraint, 39)
        self.assertGreater(41, first_constraint)

    def test_second_constraint(self):
        Xmin = self.result.Xmin
        second_constraint = Xmin[0] * Xmin[1] * Xmin[2] * Xmin[3]
        self.assertGreaterEqual(25, second_constraint)

    def test_third_constraint(self):
        Xmin = self.result.Xmin
        self.assertTrue(np.all(Xmin <= 5), 'Make sure the upper boundary is 5')
        self.assertTrue(np.all(Xmin >= 1), 'Make sure the lower boundary is 1')
