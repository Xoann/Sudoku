import unittest

from src.sudoku import Sudoku
from src.sudoku_solver import SudokuSolver


class TestSudokuSolver(unittest.TestCase):
    def setUp(self):
        self.unsolvable_sudoku = Sudoku(
            board=[
                [4, 3, None, None, 7, None, None, None, None],
                [6, None, None, 1, 9, 5, None, None, None],
                [None, 9, 8, None, None, None, None, 6, None],
                [8, None, None, None, 6, None, None, None, 3],
                [None, None, None, 8, None, 3, None, None, 1],
                [7, None, None, None, 2, None, None, None, 6],
                [None, 6, None, None, None, None, 2, 8, None],
                [None, None, None, 4, 1, 9, None, None, 5],
                [None, None, None, None, 8, None, None, 7, 9],
            ]
        )

        self.invalid_sudoku = Sudoku(
            board=[
                [4, 4, None, None, 7, None, None, None, None],
                [6, None, None, 1, 9, 5, None, None, None],
                [None, 9, 8, None, None, None, None, 6, None],
                [8, None, None, None, 6, None, None, None, 3],
                [None, None, None, 8, None, 3, None, None, 1],
                [7, None, None, None, 2, None, None, None, 6],
                [None, 6, None, None, None, None, 2, 8, None],
                [None, None, None, 4, 1, 9, None, None, 5],
                [None, None, None, None, 8, None, None, 7, 9],
            ]
        )

        self.solver = SudokuSolver(Sudoku())

    def test_invalid_board_init(self):
        with self.assertRaises(ValueError) as context:
            SudokuSolver(self.invalid_sudoku)

        expected = "Cannot initialize SudokuSolver for unsolvable Sudoku"
        self.assertEqual(str(context.exception), expected)

    def test_is_safe(self):
        is_safe = self.solver._is_safe(0, 2, 1)
        self.assertTrue(is_safe)

    def test_is_not_safe(self):
        is_safe = self.solver._is_safe(0, 2, 4)
        self.assertFalse(is_safe)

    def test_solve_backtrack(self):
        solved = self.solver.solve_backtrack()
        expected_board = [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [4, 5, 6, 7, 8, 9, 1, 2, 3],
            [7, 8, 9, 1, 2, 3, 4, 5, 6],
            [2, 1, 4, 3, 6, 5, 8, 9, 7],
            [3, 6, 5, 8, 9, 7, 2, 1, 4],
            [8, 9, 7, 2, 1, 4, 3, 6, 5],
            [5, 3, 1, 6, 4, 2, 9, 7, 8],
            [6, 4, 2, 9, 7, 8, 5, 3, 1],
            [9, 7, 8, 5, 3, 1, 6, 4, 2]
        ]
        self.assertTrue(solved)
        self.assertEqual(self.solver.sudoku.get_board(), expected_board)
