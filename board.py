from constants import *
import pygame, sys

screen = pygame.display.set_mode((WIDTH, HEIGHT))
class Board:


    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.selected_cell = None # used in select function (Tom)

    def draw(self): # draws the grids for the game (Tom)
        # draw horizontal lines
        for i in range(0, BOARD_ROWS + 1): # allows a line to be drawn to outline the board (Tom)
            if i % 3 == 0:
                pygame.draw.line(
                    screen,
                    LINE_COLOR,
                    (0, i * SQUARE_SIZE),
                    (WIDTH, i * SQUARE_SIZE), # Made the WIDTH divisible by 9 (693) under constants for a nicer looking board
                    BORDER_LINE_WIDTH
                )
            else:
                pygame.draw.line(
                    screen,
                    LINE_COLOR,
                    (0, i * SQUARE_SIZE),
                    (WIDTH, i * SQUARE_SIZE),
                    LINE_WIDTH
                )
        # draw vertical lines
        for i in range(0, BOARD_COLS + 1):
            if i % 3 == 0:
                pygame.draw.line(
                    screen,
                    LINE_COLOR,
                    (i * SQUARE_SIZE, 0),
                    (i * SQUARE_SIZE, HEIGHT), # Made the HEIGHT divisible by 9 (693) under constants for a nicer looking board
                    BORDER_LINE_WIDTH
            )
            else:
                pygame.draw.line(
                    screen,
                    LINE_COLOR,
                    (i * SQUARE_SIZE, 0),
                    (i * SQUARE_SIZE, HEIGHT),
                    # Made the HEIGHT divisible by 9 (693) under constants for a nicer looking board
                    LINE_WIDTH
                )

    def select(self, row, col): # used for marking the cell on the board at the selected cell (Tom)
        self.selected_cell = (row, col)


    def click(self, x, y): # finding the row and column of the board (Tom)
        row = y // SQUARE_SIZE # instead of a value from 0 - 693, it gives you 0-9
        col = x // SQUARE_SIZE # instead of a value from 0 - 693, it gives you 0-9

        if 0 <= row < BOARD_ROWS and 0 <= col < BOARD_ROWS: # if the value is within the board paramenters
            return (row, col) # returns the coordinates
        else: # if outside the values
            return None # returns None

        # self.cell = (x, y) # temporary attribute (corey 11/22) - removed/edited (Tom)

    def clear(self):
        #check if cell was empty at game start
        # Update once cell is complete to set_cell_value(0) (cell class)
#        if self.board_removed_test[self.selected_cell[0]][self.selected_cell[1]] != 0:    #check if cell was filled in at game start
#            print("Cannot clear cell")
#        else:
#            self.board_active_test[self.selected_cell[0]][self.selected_cell[1]] = 0
        pass

    def sketch(self, value):
        # update once draw() is finished
        pass

    def place_number(self, value):
        # Update once proper board list is written: set_cell_value(value) (cell class)
#        self.board_active_test[self.selected_cell[0]][self.selected_cell[1]] = value


        #do we need to check if the cell was empty (0) at game start?
        pass

    def reset_to_original(self):
        # Update once proper board list is written
        # for loop that goes through original 2-d array and assigns corresponding values
#        for row in range(9):
#            for column in range(9):
#                self.board_active_test[row][column] = self.board_removed_test[row][column]
        pass

    def is_full(self):
        #for loop that steps through 2-d array and checks for 0's
        # Update once proper board list is written
#        for row in range(9):
#            for column in range(9):
#                if self.board_active_test[row][column] == 0:
#                    return False
#        return True
        pass

    def update_board(self):
        pass

    def find_empty(self):
        # for loop through current aray and looks for 0
        #        for row in range(9):
        #            for column in range(9):
        #                if self.board_active_test[row][
        #                    column] == 0:  # update with proper board list. Only find first empty cell?
        #                    return (row, column)  # do we want to index from 0 on row and column
        pass

    def check_board(self):
        # for loop that compares each element to corresponding element in solution 2-d array
#       for row in range(9):
#           for column in range(9):
#               if self.board_active_test[row][column] != self.board_full_test[row][column]:
#                   return False
#       return True
        pass
