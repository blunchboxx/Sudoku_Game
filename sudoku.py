from constants import *
from board import *
import pygame
import sys

# main() (Tom/Jason).
# create different screens (game start, game over, and game in-progress)


if __name__ == '__main__':

    '''
    Initialize pygame module and screen
    Set initial variables
    Generate board and draw it on screen
    '''
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Sudoku')
    screen.fill(BG_COLOR)

    game_over = False

    board = Board(9, 9, screen, 30)
    board.draw()

    while True:
        # event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()