from constants import *
from board import *
import pygame
import sys

# main() (Tom/Jason).
# create different screens (game start, game over, and game in-progress)


def draw_game_start():

    screen.fill(BG_COLOR)  # Fill screen

    # Load title screen background image
    start_bg_image = pygame.image.load(START_IMAGE_FILENAME)

    # Set start title fonts and text
    start_title_font = pygame.font.Font(None, START_TITLE_FONT)
    start_title_text = 'Welcome to Sudoku'

    start_subtitle_font = pygame.font.Font(None, START_SUBTITLE_FONT)
    start_subtitle_text = 'Select Game Mode:'

    # Set start title surfaces and rectangles
    start_title_surf = start_title_font.render(start_title_text, 0, TITLE_COLOR)
    start_subtitle_surf = start_subtitle_font.render(start_subtitle_text, 0, TITLE_COLOR)
    start_title_rect = start_title_surf.get_rect(center=(WIDTH //2, HEIGHT // 2 - 200))
    start_subtitle_rect = start_subtitle_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    # Blit titles to screen
    screen.blit(start_bg_image, (0,0))
    screen.blit(start_title_surf, start_title_rect)
    screen.blit(start_subtitle_surf, start_subtitle_rect)

    # Initialize button font
    start_button_font = pygame.font.Font(None, TITLE_BUTTON_FONT)

    # Initialize button text
    easy_button_text = start_button_font.render('Easy', 0, BUTTON_TEXT_COLOR)
    med_button_text = start_button_font.render('Medium', 0, BUTTON_TEXT_COLOR)
    hard_button_text = start_button_font.render('Hard', 0, BUTTON_TEXT_COLOR)

    # Initialize button background color and text
    # Sets size to 20 pixels longer than width of text and 20 pixels taller than start text
    easy_button_surf = pygame.Surface((easy_button_text.get_size()[0] + 20, easy_button_text.get_size()[1] + 20))
    easy_button_surf.fill(BUTTON_BOX_COLOR)
    easy_button_surf.blit(easy_button_text, (10, 10))  # Box is 20 pixels larger so 10,10 is center of box

    med_button_surf = pygame.Surface((med_button_text.get_size()[0] + 20, med_button_text.get_size()[1] + 20))
    med_button_surf.fill(BUTTON_BOX_COLOR)
    med_button_surf.blit(med_button_text, (10, 10))

    hard_button_surf = pygame.Surface((hard_button_text.get_size()[0] + 20, hard_button_text.get_size()[1] + 20))
    hard_button_surf.fill(BUTTON_BOX_COLOR)
    hard_button_surf.blit(hard_button_text, (10, 10))

    # Initialize button rectangles/locations
    easy_button_rect = easy_button_surf.get_rect(center=(WIDTH // 2 - 200, HEIGHT // 2 + 150))
    med_button_rect = med_button_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 150))
    hard_button_rect = hard_button_surf.get_rect(center=(WIDTH // 2 + 200, HEIGHT // 2 + 150))

    # Draw buttons
    screen.blit(easy_button_surf, easy_button_rect)
    screen.blit(med_button_surf, med_button_rect)
    screen.blit(hard_button_surf, hard_button_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:  # FixMe add event to pass difficulty level to board
                if easy_button_rect.collidepoint(event.pos):  # Checks if user click is on easy button
                    return 30  # If mouse clicks on easy button, return to main and return value 30
                elif med_button_rect.collidepoint(event.pos):  # If mouse clicks on medium
                    return 40  # Return to main() and return value of 40
                elif hard_button_rect.collidepoint(event.pos):  # If mouse clicks on hard
                    return 50  # Return to main() and return value of 50

        pygame.display.update()



if __name__ == '__main__':

    '''
    Initialize pygame module and screen
    Set initial variables
    Generate board and draw it on screen
    '''
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Sudoku')
    difficulty = draw_game_start()

    game_over = False

    screen.fill(BG_COLOR)
    board = Board(9, 9, screen, difficulty)
    board.draw()

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
