from sudoku_generator import *


if __name__ == '__main__':
    sudoku_board = SudokuGenerator(9,30)

    sudoku_board.fill_diagonal()
    sudoku_board.fill_remaining(0, 0)
    sudoku_board.remove_cells()

    sudoku_board.print_board()

