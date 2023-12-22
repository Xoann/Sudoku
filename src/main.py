from flask import Flask, request, jsonify

from src.sudoku import Sudoku
from src.sudoku_solver import SudokuSolver

app = Flask(__name__)


def backtracking_solve(data: list[list[int]]) -> list[list[int]]:
    sudoku = Sudoku(board=data)
    solver = SudokuSolver(sudoku)
    solver.solve_backtrack()
    return sudoku.get_board()


@app.route('/validate', methods=['POST'])
def validate():
    try:
        data = request.get_json()
        if not data or not isinstance(data, list):
            return jsonify({'error': 'Invalid data format'}), 400

        sudoku = Sudoku(board=data)
        result = sudoku.is_valid()
        return jsonify({'result': result})

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
