from constants import *
from board import *
import pygame
import sys

# main() (Tom/Jason).
# create different screens (game start, game over, and game in-progress)


def draw_game_start():

    start_bg_image = pygame.image.load(START_IMAGE_FILENAME)
    start_title_font = pygame.font.Font(None, START_TITLE_FONT)
    start_title_text = 'Welcome to Sudoku'

    start_subtitle_font = pygame.font.Font(None, START_SUBTITLE_FONT)
    start_subtitle_text = 'Select Game Mode:'

    start_title_surf = start_title_font.render(start_title_text, 0, TITLE_COLOR)
    start_subtitle_surf = start_subtitle_font.render(start_subtitle_text, 0, TITLE_COLOR)
    start_title_rect = start_title_surf.get_rect(center=(WIDTH //2, HEIGHT // 2 - 200))
    start_subtitle_rect = start_subtitle_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    screen.fill(BG_COLOR)
    screen.blit(start_bg_image, (0,0))
    screen.blit(start_title_surf, start_title_rect)
    screen.blit(start_subtitle_surf, start_subtitle_rect)


if __name__ == '__main__':

    '''
    Initialize pygame module and screen
    Set initial variables
    Generate board and draw it on screen
    '''
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Sudoku')
    draw_game_start()

    game_over = False

    # board = Board(9, 9, screen, 30)
    # board.draw()

    while True:
        # event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

    # sudoku_board.fill_diagonal()
    # sudoku_board.fill_remaining(0, 0)
    # sudoku_board.remove_cells()

    # sudoku_board.print_board()
