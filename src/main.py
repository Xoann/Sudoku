from flask_socketio import SocketIO
from typing import Optional

from flask import Flask, request, jsonify
from flask_cors import CORS

from src.sudoku import Sudoku
from src.sudoku_solver import SudokuSolver

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")


def backtracking_solve(data: list[list[int]]) -> list[list[int]]:
    sudoku = Sudoku(board=data)
    solver = SudokuSolver(sudoku)
    solver.solve_backtrack()
    return sudoku.get_board()


def format_board_data(data: list[str]) -> list[list[Optional[int]]]:
    size = int(len(data) ** 0.25)
    board = [[None] * size ** 2 for _ in range(size ** 2)]

    for i in range(size ** 2):
        for j in range(size ** 2):
            entry = (int(data[9 * i + j]) if data[9 * i + j] != "" else None)
            board[(i // size) * size + j // size][(i % size) * size + (j % size)] = entry

    return board


@app.route('/validate', methods=['POST'])
def validate():
    try:
        data = request.get_json()
        board = format_board_data(data)
        sudoku = Sudoku(board=board)
        result = sudoku.is_valid()
        return jsonify({'result': result})

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@socketio.on('solve', namespace='/solve')
def solve(board: list[str]):
    try:
        formatted_board = format_board_data(board)
        sudoku = Sudoku(board=formatted_board)
        sudoku_solver = SudokuSolver(sudoku)
        sudoku_solver.solve_backtrack(socket=socketio)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
