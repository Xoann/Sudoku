import collections


class Sudoku:
    """
    A class to represent a Sudoku.

    Attributes:
        board: (List[List[Optional[int]]]) The sudoku represented by a matrix
        size: (int) The size of the sub-grid 3 by default
    """

    def __init__(self, size: int = 3):
        """Initialize the Sudoku
        :param size: The size of the sub-grid 3 by default
        """
        self.board = [[None] * size ** 2 for _ in range(size ** 2)]
        self.size = size

    def __str__(self) -> str:
        """Return a string representation of the Sudoku
        """
        string_representation = ""
        for row in self.board:
            string_representation += "|"
            for i, cell in enumerate(row):
                cell_string = str(cell) if cell is not None else ' '
                delimiter = '|' if i != self.size ** 2 - 1 else '|\n'
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

        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] is None:
                    continue

                if self.board[i][j] in row_dup[i]:
                    return False
                row_dup[i].add(self.board[i][j])

                if self.board[i][j] in col_dup[j]:
                    return False
                col_dup[j].add(self.board[i][j])

                if self.board[i][j] in box_dup[(i // self.size, j // self.size)]:
                    return False
                box_dup[(i // self.size, j // self.size)].add(self.board[i][j])
        return True

    def set_cell(self, row: int, col: int, value: int) -> None:
        """Sets a cell in the board to value

        :param row: row position of the cell 0 indexed
        :param col: column position of the cell 0 indexed
        :param value: value of the cell
        :return: None
        :raises ValueError: If value is not in range(1, self.size ** 2 + 1)
        :raises IndexError: If row or col is not in range(0, self.size ** 2)
        """
        if value not in range(1, self.size ** 2 + 1):
            raise ValueError(f"Value must be valid entry for a {self.size} by {self.size} sudoku board")

        if row not in range(0, self.size ** 2):
            raise IndexError(f"row must be valid row index for a {self.size} by {self.size} sudoku board")

        if col not in range(0, self.size ** 2):
            raise IndexError(f"col must be valid col index for a {self.size} by {self.size} sudoku board")

        self.board[row][col] = value
