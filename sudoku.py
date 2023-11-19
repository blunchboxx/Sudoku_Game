from sudoku_generator import *
import pygame
from constants import *
import sys

# main() (Tom/Jason).
# create different screens (game start, game over, and game in-progress)


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Sudoku')
    sudoku_board = SudokuGenerator(9, 30)
    screen.fill(BG_COLOR)

    game_over = False

    sudoku_board.fill_diagonal()
    sudoku_board.fill_remaining(0, 0)
    sudoku_board.remove_cells()

    sudoku_board.print_board()
