from constants import *
import pygame, sys
from sudoku_generator import SudokuGenerator
from cell import Cell

# screen = pygame.display.set_mode((WIDTH, HEIGHT))
class Board:

    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.selected_cell = None # used in select function (Tom)
        self.generated_board = SudokuGenerator(BOARD_ROWS, self.difficulty)  # Generate initial board
        self.generated_board.fill_values()  # Fill initial board with solution
        self.solution_board = self.generated_board.get_board()  # Assign solved board to variable for end game comparison
        self.generated_board.remove_cells()  # Remove required number of cells from initial board
        self.starting_board = self.generated_board.get_board()  # Assign initial board with removed cells to variable
        # Initializes starting board cells and assigns values
        self.starting_cells = [
            [Cell(self.starting_board[i][j], i, j, self.screen) for j in range(BOARD_COLS)]
            for i in range(BOARD_ROWS)
        ]
        self.sketched_cells = self.starting_cells  # Added to track game cells as they are updated by player

    def draw(self):  # draws the grids for the game (Tom)
        # draw horizontal lines
        for i in range(0, BOARD_ROWS + 1): # allows a line to be drawn to outline the board (Tom)
            if i % 3 == 0:
                pygame.draw.line(
                    self.screen,
                    LINE_COLOR,
                    (0, i * SQUARE_SIZE),
                    (WIDTH, i * SQUARE_SIZE), # Made the WIDTH divisible by 9 (693) under constants for a nicer looking board
                    BORDER_LINE_WIDTH
                )
            else:
                pygame.draw.line(
                    self.screen,
                    LINE_COLOR,
                    (0, i * SQUARE_SIZE),
                    (WIDTH, i * SQUARE_SIZE),
                    LINE_WIDTH
                )
        # draw vertical lines
        for i in range(0, BOARD_COLS + 1):
            if i % 3 == 0:
                pygame.draw.line(
                    self.screen,
                    LINE_COLOR,
                    (i * SQUARE_SIZE, 0),
                    (i * SQUARE_SIZE, HEIGHT), # Made the HEIGHT divisible by 9 (693) under constants for a nicer looking board
                    BORDER_LINE_WIDTH
            )
            else:
                pygame.draw.line(
                    self.screen,
                    LINE_COLOR,
                    (i * SQUARE_SIZE, 0),
                    (i * SQUARE_SIZE, HEIGHT),
                    # Made the HEIGHT divisible by 9 (693) under constants for a nicer looking board
                    LINE_WIDTH
                )

        for i in range(BOARD_COLS):
            for j in range(BOARD_ROWS):
                self.starting_cells[i][j].draw(self.screen)

    def select(self, row, col): # used for marking the cell on the board at the selected cell (Tom)
        # FIXME need to add functions to draw red box on selected cell
        return self.sketched_cells[row][col]


    def click(self, x, y): # finding the row and column of the board (Tom)
        row = y // SQUARE_SIZE  # instead of a value from 0 - 693, it gives you 0-9
        col = x // SQUARE_SIZE  # instead of a value from 0 - 693, it gives you 0-9

        if 0 <= row < BOARD_ROWS and 0 <= col < BOARD_ROWS: # if the value is within the board paramenters
            pygame.display.update()
            return tuple([row, col])  # returns the coordinates
        # Check if location of click is in button area
        elif (0 <= x <= WIDTH - 10) and (HEIGHT <= y <= HEIGHT + 80):
            location = (x, y)

            pygame.display.update()
            return location  # Return button area click location to check which button was clicked
        else: # if outside the values
            return None # returns None

        # self.cell = (x, y) # temporary attribute (corey 11/22) - removed/edited (Tom)

    def clear(self):
        #check if cell was filled in at game start
        if self.generated_board[self.selected_cell[0]][self.selected_cell[1]] != 0:
            print("Cannot clear cell")
        else:   #update cell object at selected cell (object with matching row and column)
            for cells in self.active_board:
                if(cells.row == self.selected_cell[0] and cells.col == self.selected_cell[1]):
                    cells.set_cell_value(0)

    '''
    Added function to check if selected cell is editable.
    Returns False if cell was part of original board.
    '''

    def editable_cell(self, row, col):
        if self.starting_cells[row][col].value == 0:
            return True
        else:
            return False


    def sketch(self, cell, value):  #Updated sketch function to see if it works - Jason
        if self.editable_cell(cell.row, cell.col):
            sketched_value = cell.set_sketched_value(value)
            return sketched_value
        '''
        #update cell object at selected cell (object with matching row and column)
        for cells in self.active_board:
            if (cells.row == self.selected_cell[0] and cells.col == self.selected_cell[1]):
                cells.set_sketched_value(value)
        '''

    def place_number(self, cell, value):  # Updated to call cell new cell.enter_value function - Jason
        cell.set_cell_value(value)
        cell.enter_value(cell.value)

        #do we need to check if the cell was empty (0) at game start?
        # Possibly - we can use editable_cell to check. - Jason
        # But if main function limits placing number to after sketching, we already check for validity at sketching

    def reset_to_original(self):
        self.sketched_cells = self.starting_cells  # Set player updated cells to equal starting cells
        self.starting_board = self.generated_board  # Set player updated board equal to initial board

    def is_full(self):
        #look for any 0 in cell.value
        for cells in self.active_board:
            if cells.value == 0:
                return False
        return True

    def update_board(self): #Unsure what this method is supposed to be doing
        pass

    def find_empty(self):
        #loop through cell.value and find the first 0 and return its coordinates
        for cells in self.active_board:
            if(cells.value == 0):
                return (cells.row, cells.col)

    def check_board(self): #FIX ME: need to fine way to store "solved puzzle" for comparison purposes
        #loop through cell.value and compare to the "solution"
        for row in range(BOARD_ROWS):
            for column in range(BOARD_COLS):
                for cells in self.active_board:
                    if(cells.row == row and cells.col == column and cells.value != self.solved_board[row][column]):
                        return False
        return True
