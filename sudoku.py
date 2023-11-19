from sudoku_generator import *
import pygame, sys

# main() (Tom/Jason).
# create different screens (game start, game over, and game in-progress)


if __name__ == '__main__':
    sudoku_board = SudokuGenerator(9, 30)

    sudoku_board.fill_diagonal()
    sudoku_board.fill_remaining(0, 0)
    sudoku_board.remove_cells()

    sudoku_board.print_board()
