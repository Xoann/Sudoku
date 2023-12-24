import time
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

    def solve_backtrack(self, socket=None, delay: int = 0.00125):
        """Solve the sudoku board using the backtracking/recursive approach

        This method mutates the board to the solved state and return whether the
        board could be solved, if it is not solvable it doesn't change the board

        :param socket: the socket used to send board updates to web app
        :param delay: the delay between each step to make visualization easier
        :return: whether the board could be solved
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
                    if socket is not None:
                        time.sleep(delay)
                        socket.emit('board_update', {'board': self._format_board_for_js(self.sudoku.get_board())}, namespace='/solve')
                    if solve_backtracking_helper(row, col + 1):
                        return True
                self.sudoku.set_cell(row, col, None)
                if socket is not None:
                    time.sleep(delay)
                    socket.emit('board_update', {'board': self._format_board_for_js(self.sudoku.get_board())}, namespace='/solve')

            return False

        return solve_backtracking_helper(0, 0)

    def _convert_cell_index(self, i: int, j: int) -> int:
        """Private helper to convert matrix cell index to integer index

        :param i: row index
        :param j: column index
        :return: integer index used by web app
        """
        size = self.sudoku.get_size()
        new_i = (i // size) * size + j // size
        new_j = (i - (new_i // size) * size) * size + j - (new_i % size) * size
        return size ** 2 * new_i + new_j

    def _format_board_for_js(self, board: list[list[int]]) -> list[str]:
        """Private helper to format the board for web app

        :param board: representation of the sudoku
        :return: board representation of the sudoku used by web app
        """
        size = self.sudoku.get_size()
        new_board = [''] * size ** 4
        for i in range(size ** 2):
            for j in range(size ** 2):
                index = self._convert_cell_index(i, j)
                new_board[index] = board[i][j]

        return new_board
