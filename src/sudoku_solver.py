from typing import Optional
from sudoku import Sudoku


class SudokuSolver:
    """Class that solves Sudoku puzzles using various algorithms

    Attributes:
        sudoku (Sudoku): The Sudoku board that will be solved
    """

    def __init__(self, sudoku: Sudoku):
        """Initialize the Sudoku Solver

        :param sudoku: solvable sudoku board
        :raises ValueError: if the board is not solvable
        """
        if not sudoku.is_valid():
            raise ValueError("Cannot initialize SudokuSolver for unsolvable Sudoku")

        self.sudoku = sudoku

    def _is_safe(self, row: int, col: int, value: Optional[int]) -> bool:
        """Check whether the Sudoku board would be valid should the value be inserted

        :param row: row index for the sudoku board
        :param col: col index for the sudoku board
        :param value: value to be inserted
        :return: whether the Sudoku board would be valid should the value be inserted
        """
        old_value = self.sudoku.get_cell(row, col)
        self.sudoku.set_cell(row, col, value)
        is_valid = self.sudoku.is_valid()
        self.sudoku.set_cell(row, col, old_value)
        return is_valid

    def solve_backtrack(self):
        """Solve the sudoku board using the backtracking/recursive approach

        This method mutates the board to the solved state
        """
        def solve_backtracking_helper(row, col):
            total_size = self.sudoku.get_size() ** 2
            if row == total_size - 1 and col == total_size:
                return True
            if col == total_size:
                row += 1
                col = 0
            if self.sudoku.get_cell(row, col) is not None:
                return solve_backtracking_helper(row, col + 1)

            for num in range(1, total_size + 1):
                if self._is_safe(row, col, num):
                    self.sudoku.set_cell(row, col, num)
                    if solve_backtracking_helper(row, col + 1):
                        return True
                self.sudoku.set_cell(row, col, None)
            return False

        solve_backtracking_helper(0, 0)
