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
            if event.type == pygame.QUIT:  # If user clicks 'X' button, quit game
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:  # Check for user mouse click
                if easy_button_rect.collidepoint(event.pos):  # Checks if user click is on easy button
                    return 1  # If mouse clicks on easy button, return to main and return difficulty 1
                elif med_button_rect.collidepoint(event.pos):  # If mouse clicks on medium
                    return 2  # Return to main() and return value of 2
                elif hard_button_rect.collidepoint(event.pos):  # If mouse clicks on hard
                    return 3  # Return to main() and return value of 3

        pygame.display.update()

def game_buttons_draw():
    # Initialize button font
    game_button_font = pygame.font.Font(None, GAME_BUTTON_FONT)

    # Initialize button text
    reset_button_text = game_button_font.render('RESET', 0, BUTTON_TEXT_COLOR)
    restart_button_text = game_button_font.render('RESTART', 0, BUTTON_TEXT_COLOR)
    exit_button_text = game_button_font.render('EXIT', 0, BUTTON_TEXT_COLOR)

    # Initialize button background color and text
    # Sets size to 20 pixels longer than width of text and 20 pixels taller than start text
    reset_button_surf = pygame.Surface((reset_button_text.get_size()[0] + 20,
                                        reset_button_text.get_size()[1] + 20))
    reset_button_surf.fill(BUTTON_BOX_COLOR)
    reset_button_surf.blit(reset_button_text, (10, 10))  # Box is 20 pixels larger so 10,10 is center of box

    restart_button_surf = pygame.Surface((restart_button_text.get_size()[0] + 20,
                                          restart_button_text.get_size()[1] + 20))
    restart_button_surf.fill(BUTTON_BOX_COLOR)
    restart_button_surf.blit(restart_button_text, (10, 10))

    exit_button_surf = pygame.Surface((exit_button_text.get_size()[0] + 20,
                                       exit_button_text.get_size()[1] + 20))
    exit_button_surf.fill(BUTTON_BOX_COLOR)
    exit_button_surf.blit(exit_button_text, (10, 10))

    # Initialize button rectangles/locations
    reset_button_rect = reset_button_surf.get_rect(center=(WIDTH // 2 - 150, HEIGHT + 40))
    restart_button_rect = restart_button_surf.get_rect(center=(WIDTH // 2, HEIGHT + 40))
    exit_button_rect = exit_button_surf.get_rect(center=(WIDTH // 2 + 150, HEIGHT + 40))

    # Draw buttons
    screen.blit(reset_button_surf, reset_button_rect)
    screen.blit(restart_button_surf, restart_button_rect)
    screen.blit(exit_button_surf, exit_button_rect)

    return [reset_button_rect, restart_button_rect, exit_button_rect]

if __name__ == '__main__':

    '''
    Initialize pygame module and screen
    Set initial variables
    Generate board and draw it on screen
    '''
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT + 80))
    pygame.display.set_caption('Sudoku')
    difficulty = draw_game_start()

    game_over = False
    cell_selected = False

    screen.fill(BG_COLOR)
    starting_board = Board(9, 9, screen, difficulty) # Initialize starting board
    sketched_board = starting_board  # Initialize board to be updated by player
    sketched_board.draw()  # Draw board on screen
    button_locations = game_buttons_draw()  # Draw reset, restart & exit buttons and save locations

    while True:
        # event loop
        for event in pygame.event.get():  # Check if window is closed by user and exit program
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:  # Check for mouse click
                x, y = event.pos  # Store mouse click location as x & y coordinates
                print(x, y)
                location = sketched_board.click(x, y)  # Pass click location to Board class 'click' function

                if location is not None:

                    if (location[0] > 8) or (location[1] > 8):
                        if button_locations[0].collidepoint(event.pos):
                            screen.fill(BG_COLOR)
                            sketched_board = starting_board
                            sketched_board.draw()
                            game_buttons_draw()
                        elif button_locations[1].collidepoint(event.pos):
                            difficulty = draw_game_start()

                            game_over = False
                            cell_selected = False

                            screen.fill(BG_COLOR)
                            starting_board = Board(9, 9, screen, difficulty)  # Initialize starting board
                            sketched_board = starting_board  # Initialize board to be updated by player
                            sketched_board.draw()  # Draw board on screen
                            button_locations = game_buttons_draw()  # Draw reset, restart & exit buttons and save locations
                            break
                        elif button_locations[2].collidepoint(event.pos):
                            pygame.quit()
                            sys.exit()

                    else:
                        cell_selected = True

                        selected_cell = sketched_board.select(location[0], location[1])

            if cell_selected == True and event.type == pygame.KEYDOWN:
                if 49 <= event.key <= 57:
                    sketched_board.sketch(selected_cell, event.key)

            # ToDo add game over functions when ready


            if game_over:
                pygame.display.update()
                pygame.time.delay(1000)
                draw_game_over()

            pygame.display.update()

    # game_over_font = pygame.font.Font(None, GAME_OVER_FONT)  # Set up end message font
