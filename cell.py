import pygame
from constants import *
class Cell:

    def __init__(self, value, row, col, screen):  # Initialize Cell variables
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketched_value = 0 # initialized value for the player while determining a solution. (Tom)
        self.selected = False # to help track if the cell has been selected yet (Tom)

    def set_cell_value(self, value):  # Setter for cell value
        self.value = value

    def set_sketched_value(self, key):  # Setter for cell's sketched value
        value_font = pygame.font.Font(None, NUM_FONT)

        if key == 49:
            value = 1
        elif key == 50:
            value = 2
        elif key == 51:
            value = 3
        elif key == 52:
            value = 4
        elif key == 53:
            value = 5
        elif key == 54:
            value = 6
        elif key == 55:
            value = 7
        elif key == 56:
            value = 8
        elif key == 58:
            value = 9

        value_surf = value_font.render(str(value), 0, SKETCHED_VALUE_COLOR)

        value_rect = value_surf.get_rect(center=(self.col * SQUARE_SIZE + SQUARE_SIZE // 4,
                                                     self.row * SQUARE_SIZE + SQUARE_SIZE // 3))

        self.screen.blit(value_surf, value_rect)

    def draw(self, screen):  # Draws cell with value inside it

        value_font = pygame.font.Font(None, NUM_FONT)  # Set font of number to be displayed

        # Set surface for values to display value character in NUM_COLOR (black)
        value_surf = value_font.render(str(self.value), 0, NUM_COLOR)

        # Set surface for empty squares to empty string and fill square with background color
        zero_surf = value_font.render('', 0, BG_COLOR)

        if self.value == 0:  # If cell value is zero, display nothing inside cell
            zero_rect = zero_surf.get_rect(center=(self.col * SQUARE_SIZE + SQUARE_SIZE // 2,
                                                   self.row * SQUARE_SIZE + SQUARE_SIZE // 2))
            screen.blit(zero_surf, zero_rect)

        elif self.value > 0:  # If cell has a non-zero value, display it in the board

            value_rect = value_surf.get_rect(center=(self.col * SQUARE_SIZE + SQUARE_SIZE // 2,
                                                     self.row * SQUARE_SIZE + SQUARE_SIZE // 2))

            screen.blit(value_surf, value_rect)
