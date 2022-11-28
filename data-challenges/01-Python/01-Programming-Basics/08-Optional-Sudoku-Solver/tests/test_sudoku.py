# pylint: disable-all
import copy
import unittest
from sudoku import sudoku_solver
from tests import in_vs_out, checker

correct_input_grid = [
    [7,0,0,  0,0,0,  0,0,6],
    [0,0,0,  6,0,0,  0,4,0],
    [0,0,2,  0,0,8,  0,0,0],

    [0,0,8,  0,0,0,  0,0,0],
    [0,5,0,  8,0,6,  0,0,0],
    [0,0,0,  0,2,0,  0,0,0],

    [0,0,0,  0,0,0,  0,1,0],
    [0,4,0,  5,0,0,  0,0,0],
    [0,0,5,  0,0,7,  0,0,4]
]

class SudokuSolverTest(unittest.TestCase):
    def test_valid_grid(self):
        input_grid = copy.deepcopy(correct_input_grid)
        solved_grid = sudoku_solver(input_grid)
        check_test = checker(solved_grid)
        self.assertTrue(check_test[0], msg=check_test[1])

    def test_input_grid_is_conserved(self):
        input_grid = copy.deepcopy(correct_input_grid)
        solved_grid = sudoku_solver(input_grid)
        iso_test = in_vs_out(correct_input_grid, solved_grid)
        self.assertTrue(iso_test[0], msg=iso_test[1])

    def test_incorrect_grid(self):
        input_grid = [
            [7,0,0,  0,0,0,  0,0,6],
            [0,0,0,  6,0,0,  0,4,0],
            [0,0,2,  0,0,8,  0,0,0],

            [0,0,8,  0,0,0,  0,0,0],
            [0,5,0,  8,0,6,  0,0,0],
            [0,0,0,  0,2,0,  0,0,0],

            [0,0,0,  0,0,0,  0,1,0],
            [0,4,0,  5,0,0,  0,0],
            [0,0,5,  0,0,7,  0,0,0]
        ]
        solver = sudoku_solver(input_grid)
        self.assertEqual(solver, "invalid grid", "Input Validation: Should return `invalid grid` when grid is missing a number")

    def test_incorrect_grid_2(self):
        input_grid = [
            [7,0,0,  0,0,0,  0,0,6],
            [0,0,0,  6,0,0,  0,4,0],
            [0,0,2,  0,0,8,  0,0,0],

            [0,0,8,  0,0,0,  0,0,0],
            [0,5,0,  8,0,6,  0,0,0],
            [0,0,0,  0,2,0,  0,0,0],

            [0,0,0,  0,0,0,  0,1,0],
            [0,0,5,  0,0,7,  0,0,0]
        ]
        solver = sudoku_solver(input_grid)
        self.assertEqual(solver, "invalid grid", "Input Validation: Should return `invalid grid` when grid is missing a column")

    def test_incorrect_grid_3(self):
        input_grid = 70004300053
        solver = sudoku_solver(input_grid)
        self.assertEqual(solver, "invalid grid", "Input Validation: Should return `invalid grid` when the grid is not a list of list")
