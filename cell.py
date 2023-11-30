import pygame
from constants import *


class Cell:

    def __init__(self, value, row, col, screen):  # Initialize Cell variables
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketched_value = 0  # initialized value for the player while determining a solution. (Tom)
        self.sketched = False  # Variable to track if a value is sketched or not
        self.selected = False  # to help track if the cell has been selected yet (Tom)

        if self.value == 0:  # Determine if cell should be user editable
            self.user_editable = True
        else:
            self.user_editable = False

    def set_cell_value(self, value):  # Setter for cell value
        self.value = value
        self.sketched = False
        self.sketched_value = 0

    def set_sketched_value(self, key):  # Setter for cell's sketched value
        self.sketched = True

        if key == 49:  # Reads ASCII key number and determines numeric value
            self.sketched_value = 1
        elif key == 50:
            self.sketched_value = 2
        elif key == 51:
            self.sketched_value = 3
        elif key == 52:
            self.sketched_value = 4
        elif key == 53:
            self.sketched_value = 5
        elif key == 54:
            self.sketched_value = 6
        elif key == 55:
            self.sketched_value = 7
        elif key == 56:
            self.sketched_value = 8
        elif key == 57:
            self.sketched_value = 9
        '''
        value_font = pygame.font.Font(None, SKETCHED_VALUE_FONT)
        value_surf = value_font.render(str(self.sketched_value), 0, SKETCHED_VALUE_COLOR)
        value_rect = value_surf.get_rect(center=(self.col * SQUARE_SIZE + SQUARE_SIZE // 4,
                                                 self.row * SQUARE_SIZE + SQUARE_SIZE // 3))

        self.screen.blit(value_surf, value_rect)
        '''
        return self.sketched_value

    def enter_value(self, value):  # Draws cell value after user sketches and hits enter
        self.sketched_value = 0
        self.sketched = False
        value_font = pygame.font.Font(None, NUM_FONT)

        value_surf = value_font.render(str(value), 0, SKETCHED_VALUE_COLOR)

        value_rect = value_surf.get_rect(center=(self.col * SQUARE_SIZE + SQUARE_SIZE // 2,
                                                 self.row * SQUARE_SIZE + SQUARE_SIZE // 2))

        self.screen.blit(value_surf, value_rect)

    def draw(self, screen):  # Draws cell with value inside it

        sketched_value_font = pygame.font.Font(None, SKETCHED_VALUE_FONT)  # Set font of sketched number

        value_font = pygame.font.Font(None, NUM_FONT)  # Set font of number to be displayed

        if self.user_editable is True:  # If cell is editable, use orange font
            value_surf = value_font.render(str(self.value), 0, SKETCHED_VALUE_COLOR)

        else:  # If cell is not editable, use black font
            # Set surface for values to display value character in NUM_COLOR (black)
            value_surf = value_font.render(str(self.value), 0, NUM_COLOR)

        if self.sketched is True:
            if self.sketched_value > 0:  # If cell has a non-zero value, display it in the board
                sketched_value_surf = sketched_value_font.render(str(self.sketched_value), 0, SKETCHED_VALUE_COLOR)

                value_rect = sketched_value_surf.get_rect(center=(self.col * SQUARE_SIZE + SQUARE_SIZE // 4,
                                                                  self.row * SQUARE_SIZE + SQUARE_SIZE // 3))

                screen.blit(sketched_value_surf, value_rect)

        else:
            sketched_value_surf = sketched_value_font.render('', 0, SKETCHED_VALUE_COLOR)

            value_rect = sketched_value_surf.get_rect(center=(self.col * SQUARE_SIZE + SQUARE_SIZE // 4,
                                                              self.row * SQUARE_SIZE + SQUARE_SIZE // 3))

            screen.blit(sketched_value_surf, value_rect)

            if self.value == 0:  # If cell value is zero, display nothing inside cell
                # Set surface for empty squares to empty string and fill square with background color
                zero_surf = value_font.render('', 0, BG_COLOR)
                zero_rect = zero_surf.get_rect(center=(self.col * SQUARE_SIZE + SQUARE_SIZE // 2,
                                                       self.row * SQUARE_SIZE + SQUARE_SIZE // 2))
                screen.blit(zero_surf, zero_rect)

            elif self.value > 0:  # If cell has a non-zero value, display it in the board

                value_rect = value_surf.get_rect(center=(self.col * SQUARE_SIZE + SQUARE_SIZE // 2,
                                                         self.row * SQUARE_SIZE + SQUARE_SIZE // 2))

                screen.blit(value_surf, value_rect)


