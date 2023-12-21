import collections
from typing import Optional, List


class Sudoku:
    """
    A class to represent a Sudoku.

    Attributes:
        _board: (List[List[Optional[int]]]) The sudoku represented by a matrix
        _size: (int) The size of the sub-grid 3 by default
    """

    def __init__(self, size: int = 3, board: Optional[List[List[Optional[int]]]] = None) -> None:
        """Initialize the Sudoku
        :param size: The size of the sub-grid 3 by default
        """
        if board is not None:
            self._board = board
        else:
            self._board = [[None] * size ** 2 for _ in range(size ** 2)]
        self._size = size

    def __str__(self) -> str:
        """Return a string representation of the Sudoku
        """
        string_representation = ""
        for row in self._board:
            string_representation += "|"
            for i, cell in enumerate(row):
                cell_string = str(cell) if cell is not None else ' '
                delimiter = '|' if i != self._size ** 2 - 1 else '|\n'
                string_representation += cell_string + delimiter

        return string_representation

    def is_valid(self) -> bool:
        """Checks if the current sudoku is valid in its current state

        Note the board may actually be unsolvable

        :return: Whether sudoku is valid or not
        """
        col_dup = collections.defaultdict(set)
        row_dup = collections.defaultdict(set)
        box_dup = collections.defaultdict(set)

        for i in range(len(self._board)):
            for j in range(len(self._board[i])):
                if self._board[i][j] is None:
                    continue

                if self._board[i][j] in row_dup[i]:
                    return False
                row_dup[i].add(self._board[i][j])

                if self._board[i][j] in col_dup[j]:
                    return False
                col_dup[j].add(self._board[i][j])

                if self._board[i][j] in box_dup[(i // self._size, j // self._size)]:
                    return False
                box_dup[(i // self._size, j // self._size)].add(self._board[i][j])
        return True

    def set_cell(self, row: int, col: int, value: Optional[int]) -> None:
        """Sets a cell in the board to value

        :param row: row position of the cell 0 indexed
        :param col: column position of the cell 0 indexed
        :param value: value of the cell
        :return: None
        :raises ValueError: If value is not in range(1, self._size ** 2 + 1)
        :raises IndexError: If row or col is not in range(0, self._size ** 2)
        """
        if value not in range(1, self._size ** 2 + 1) and value is not None:
            raise ValueError(f"Value must be valid entry for a {self._size} by {self._size} sudoku board")

        if row not in range(0, self._size ** 2):
            raise IndexError(f"row must be valid row index for a {self._size} by {self._size} sudoku board")

        if col not in range(0, self._size ** 2):
            raise IndexError(f"col must be valid col index for a {self._size} by {self._size} sudoku board")

        self._board[row][col] = value

    def get_cell(self, row: int, col: int) -> Optional[int]:
        """Get the value of the cell

        :param row: row position of the cell 0 indexed
        :param col: col position of the cell 0 indexed
        :return: value of the cell
        :raises IndexError: If row or col is not in range(0, self._size ** 2)
        """
        if row not in range(0, self._size ** 2):
            raise IndexError(f"row must be valid row index for a {self._size} by {self._size} sudoku board")

        if col not in range(0, self._size ** 2):
            raise IndexError(f"col must be valid col index for a {self._size} by {self._size} sudoku board")

        return self._board[row][col]

    def get_board(self) -> List[List[int]]:
        """Gets the board of the sudoku

        :return: Matrix representation of the sudoku
        """
        return self._board

    def get_size(self) -> int:
        """Gets the size of the sudoku

        :return: The size of the sudoku
        """
        return self._size
