import unittest
from src.sudoku import Sudoku


class TestSudoku(unittest.TestCase):
    def setUp(self):
        self.sudoku = Sudoku(
            board=[
                [5, 3, None, None, 7, None, None, None, None],
                [6, None, None, 1, 9, 5, None, None, None],
                [None, 9, 8, None, None, None, None, 6, None],
                [8, None, None, None, 6, None, None, None, 3],
                [4, None, None, 8, None, 3, None, None, 1],
                [7, None, None, None, 2, None, None, None, 6],
                [None, 6, None, None, None, None, 2, 8, None],
                [None, None, None, 4, 1, 9, None, None, 5],
                [None, None, None, None, 8, None, None, 7, 9],
            ]
        )

    def test_is_valid(self):
        self.assertTrue(self.sudoku.is_valid())

    def test_is_invalid(self):
        self.sudoku.set_cell(0, 1, 5)
        self.assertFalse(self.sudoku.is_valid())

    def test_set_cell_valid(self):
        self.sudoku.set_cell(0, 2, 2)
        board = [
            [5, 3, 2, None, 7, None, None, None, None],
            [6, None, None, 1, 9, 5, None, None, None],
            [None, 9, 8, None, None, None, None, 6, None],
            [8, None, None, None, 6, None, None, None, 3],
            [4, None, None, 8, None, 3, None, None, 1],
            [7, None, None, None, 2, None, None, None, 6],
            [None, 6, None, None, None, None, 2, 8, None],
            [None, None, None, 4, 1, 9, None, None, 5],
            [None, None, None, None, 8, None, None, 7, 9],
        ]
        self.assertEqual(self.sudoku.get_board(), board)

    def test_set_cell_invalid_value(self):
        with self.assertRaises(ValueError) as context:
            self.sudoku.set_cell(0, 0, 0)

        expected = f"Value must be valid entry for a {self.sudoku.get_size()} by {self.sudoku.get_size()} sudoku board"
        self.assertEqual(str(context.exception), expected)

    def test_set_cell_invalid_row(self):
        with self.assertRaises(IndexError) as context:
            self.sudoku.set_cell(-1, 0, 1)

        expected = (f"row must be valid row index for a {self.sudoku.get_size()} "
                    f"by {self.sudoku.get_size()} sudoku board")
        self.assertEqual(str(context.exception), expected)

    def test_set_cell_invalid_col(self):
        with self.assertRaises(IndexError) as context:
            self.sudoku.set_cell(0, -1, 1)

        expected = (f"col must be valid col index for a {self.sudoku.get_size()} "
                    f"by {self.sudoku.get_size()} sudoku board")
        self.assertEqual(str(context.exception), expected)

    def test_get_cell_valid(self):
        self.assertEqual(self.sudoku.get_cell(0, 0), 5)

    def test_get_cell_invalid_row(self):
        with self.assertRaises(IndexError) as context:
            self.sudoku.get_cell(99, 0)

        expected = (f"row must be valid row index for a {self.sudoku.get_size()} "
                    f"by {self.sudoku.get_size()} sudoku board")
        self.assertEqual(str(context.exception), expected)

    def test_get_cell_invalid_col(self):
        with self.assertRaises(IndexError) as context:
            self.sudoku.get_cell(0, 99)

        expected = (f"col must be valid col index for a {self.sudoku.get_size()} "
                    f"by {self.sudoku.get_size()} sudoku board")
        self.assertEqual(str(context.exception), expected)
