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

    while True:  # Run until user selects difficulty and starts game
        for user_event in pygame.event.get():
            if user_event.type == pygame.QUIT:  # If user clicks 'X' button, quit game
                pygame.quit()
                sys.exit()
            if user_event.type == pygame.MOUSEBUTTONDOWN:  # Check for user mouse click
                if easy_button_rect.collidepoint(user_event.pos):  # Checks if user click is on easy button
                    return 30  # If mouse clicks on easy button, return 30 cells to remove
                elif med_button_rect.collidepoint(user_event.pos):  # If mouse clicks on medium
                    return 40  # Return to main() and return value of 40 cells to remove
                elif hard_button_rect.collidepoint(user_event.pos):  # If mouse clicks on hard
                    return 50  # Return to main() and return value of 50 cells to remove

        pygame.display.update()

def draw_game_board(board):  # Draw game board and button locations
    screen.fill(BG_COLOR)

    board.draw()  # Draw board on screen
    board.draw_cell_numbers()
    location_of_buttons = game_buttons_draw()  # Draw reset, restart & exit buttons and save locations
    return location_of_buttons

def draw_select_box(row, col):  # Draw red rectangle on selected cell
    select_surf = pygame.Surface((SQUARE_SIZE - 7.5, SQUARE_SIZE - 7.5))
    select_color = SELECTED_LINE_COLOR
    select_rect = select_surf.get_rect(center=(col * SQUARE_SIZE + SQUARE_SIZE // 2,
                                               row * SQUARE_SIZE + SQUARE_SIZE // 2))

    pygame.draw.rect(screen, select_color, select_rect, width=2)

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

def draw_game_over(board):
    # if board.check_board():
    screen.fill(BG_COLOR) # create empty screen
    start_bg_image = pygame.image.load(START_IMAGE_FILENAME)  # initialize sudoku image
    game_over_font = pygame.font.Font(None, START_TITLE_FONT) # initialize game over font
    game_button_font = pygame.font.Font(None, GAME_BUTTON_FONT) # initialize game button font

    if board.check_board(): # check the board for the solution being correct (return True)

        # add draw win screen functions here. Need to have exit button
        game_over_text = "Game Won!" # Game won text

        # initialize game over message
        game_over_surf = game_over_font.render(game_over_text, 0, TITLE_COLOR)
        game_over_rect = game_over_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2))

        # initialize the exit button again
        exit_button_text = game_button_font.render('EXIT', 0, BUTTON_TEXT_COLOR)
        exit_button_surf = pygame.Surface((exit_button_text.get_size()[0] + 20,
                                           exit_button_text.get_size()[1] + 20))
        exit_button_surf.fill(BUTTON_BOX_COLOR)
        exit_button_surf.blit(exit_button_text, (10, 10))
        exit_button_rect = exit_button_surf.get_rect(center=(WIDTH // 2, HEIGHT + 40))

        # generate screen with image and message with exit button
        screen.blit(start_bg_image, (0, 0))
        screen.blit(game_over_surf, game_over_rect)
        screen.blit(exit_button_surf, exit_button_rect)

        return [game_over_rect, exit_button_rect]

    else: # if player was incorrect
        # add draw loss screen functions here. Need to add Restart button
        game_over_text = "Game Over :(" # game over text

        # initialize game over message
        game_over_surf = game_over_font.render(game_over_text, 0, TITLE_COLOR)
        game_over_rect = game_over_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2))

        # initialize the restart button again
        restart_button_text = game_button_font.render('RESTART', 0, BUTTON_TEXT_COLOR)
        restart_button_surf = pygame.Surface((restart_button_text.get_size()[0] + 20,
                                              restart_button_text.get_size()[1] + 20))
        restart_button_surf.fill(BUTTON_BOX_COLOR)
        restart_button_surf.blit(restart_button_text, (10, 10))
        restart_button_rect = restart_button_surf.get_rect(center=(WIDTH // 2, HEIGHT + 40))

        # generate screen with image and message with exit button
        screen.blit(start_bg_image, (0, 0))
        screen.blit(game_over_surf, game_over_rect)
        screen.blit(restart_button_surf, restart_button_rect)

        return [game_over_rect, restart_button_rect]


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
    pygame.display.update()

    starting_board = Board(9, 9, screen, difficulty) # Initialize starting board
    sketched_board = starting_board  # Initialize board to be updated by player
    button_locations = draw_game_board(sketched_board)  # Initializes location of game buttons
    pygame.display.update()
    arrow_keys = [pygame.K_DOWN, pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT]  # Sets up arrow key list

    game_over = False
    cell_selected = False

    while True:
        # event loop
        for event in pygame.event.get():  # Check if window is closed by user and exit program
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:  # Check for mouse click
                x, y = event.pos  # Store mouse click location as x & y coordinates
                location = sketched_board.click(x, y)  # Pass click location to Board class 'click' function

                if location is not None:

                    if (location[0] > 8) or (location[1] > 8):  # If click location outside game board
                        if button_locations[0].collidepoint(event.pos):  # If click location is on reset button

                            sketched_board.reset_to_original()
                            button_locations = draw_game_board(sketched_board)
                            pygame.display.update()

                        elif button_locations[1].collidepoint(event.pos):  # If click location is on restart button
                            difficulty = draw_game_start()

                            game_over = False
                            cell_selected = False

                            screen.fill(BG_COLOR)
                            starting_board = Board(9, 9, screen, difficulty)  # Initialize starting board
                            sketched_board = starting_board  # Initialize board to be updated by player
                            button_locations = draw_game_board(sketched_board)
                            pygame.display.update()
                            break
                        elif button_locations[2].collidepoint(event.pos):  # If click is on exit button
                            pygame.quit()
                            sys.exit()

                    else:  # If click is inside board, select cell
                        cell_selected = True

                        selected_cell = sketched_board.select(location[0], location[1])
                        draw_game_board(sketched_board)
                        draw_select_box(selected_cell.row, selected_cell.col)

            # Checks for value entries and arrow key presses after a cell has been selected
            if cell_selected is True and event.type == pygame.KEYDOWN:
                # Sets cell's sketched value after num keys 1 - 9 are pressed
                if 49 <= event.key <= 57:
                    sketched_value = sketched_board.sketch(selected_cell, event.key)
                    draw_game_board(sketched_board)
                    draw_select_box(selected_cell.row, selected_cell.col)

                # Sets cell value after pressing enter
                elif event.key == 13:
                    sketched_board.place_number(selected_cell, sketched_value)
                    draw_game_board(sketched_board)
                    draw_select_box(selected_cell.row, selected_cell.col)

                    if sketched_board.is_full(): # After each new entry, check if board is full
                        sketched_board.check_board() # checks if board is correct or incorrect
                        pygame.display.update() # will update
                        pygame.time.delay(3000) # wait three second
                        draw_game_over(sketched_board)  # displays winner or loser messages depending on check function



                # Checks if pressed key was an arrow key. Allows arrow keys to change highlighted cell
                elif event.key in arrow_keys:
                    if event.key == pygame.K_UP:  # UP ARROW function
                        if selected_cell.row == 0:  # Do nothing if already at top of board
                            continue
                        else:
                            # If not at top of board, decrement selected cell row by 1 and update screen
                            selected_cell = sketched_board.select(selected_cell.row - 1, selected_cell.col)
                            draw_game_board(sketched_board)
                            draw_select_box(selected_cell.row, selected_cell.col)
                    elif event.key == pygame.K_DOWN:  # DOWN ARROW function
                        if selected_cell.row == 8:  # Do nothing if already at bottom of board
                            continue
                        else:
                            # If not at bottom of board, increment selected cell row by 1 and update screen
                            selected_cell = sketched_board.select(selected_cell.row + 1, selected_cell.col)
                            draw_game_board(sketched_board)
                            draw_select_box(selected_cell.row, selected_cell.col)
                    elif event.key == pygame.K_LEFT:  # LEFT ARROW functions
                        if selected_cell.col == 0:  # Do nothing if already at left of board
                            continue
                        else:
                            # If not at left of board, decrement selected cell col by 1 and update screen
                            selected_cell = sketched_board.select(selected_cell.row, selected_cell.col - 1)
                            draw_game_board(sketched_board)
                            draw_select_box(selected_cell.row, selected_cell.col)
                    else:  # RIGHT ARROW functionality
                        if selected_cell.col == 8:  # Do nothing if already at right of board
                            continue
                        else:
                            # If not at right of board, increment selected cell col by 1 and update screen
                            selected_cell = sketched_board.select(selected_cell.row, selected_cell.col + 1)
                            draw_game_board(sketched_board)
                            draw_select_box(selected_cell.row, selected_cell.col)

                    if sketched_board.is_full(): # After each new entry, check if board is full
                        sketched_board.check_board() # checks if board is correct or incorrect
                        pygame.display.update() # will update
                        pygame.time.delay(1000) # wait one second
                        draw_game_over(sketched_board)  # displays winner or loser messages depending on check function

                elif event.key == 8 or event.key == 127: #if user presses backspace or delete
                    sketched_board.clear(selected_cell)
                    draw_game_board(sketched_board)
                    draw_select_box(selected_cell.row, selected_cell.col)



                pygame.display.update()