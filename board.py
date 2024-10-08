import pygame
from cell import Cell
from constants import *
from sudoku_generator import SudokuGenerator


# screen = pygame.display.set_mode((WIDTH, HEIGHT))
class Board:

    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.selected_cell = None  # used in select function (Tom)
        self.generated_board = SudokuGenerator(BOARD_ROWS, self.difficulty)  # Generate initial board
        self.generated_board.fill_values()  # Fill initial board with solution
        self.solution_board = [row[:] for row in self.generated_board.get_board()]  # Assign solved board to variable
        self.generated_board.remove_cells()  # Remove required number of cells from initial board
        self.starting_board = self.generated_board.get_board()  # Assign initial board with removed cells to variable
        # Initializes starting board cells and assigns values
        self.starting_cells = [[Cell(self.starting_board[i][j], i, j, self.screen) for j in range(BOARD_COLS)] for i in
                               range(BOARD_ROWS)]
        # self.sketched_cells = self.starting_cells  # Added to track game cells as they are updated by player

    # draws the grids for the game (Tom)
    def draw(self):
        # draw horizontal lines
        for i in range(0, BOARD_ROWS + 1):
            if i % 3 == 0:
                pygame.draw.line(
                    self.screen,
                    LINE_COLOR,
                    (0, i * SQUARE_SIZE),
                    (WIDTH, i * SQUARE_SIZE),
                    # Made the WIDTH divisible by 9 (693) under constants for a nicer looking board
                    BORDER_LINE_WIDTH)
            else:
                pygame.draw.line(
                    self.screen,
                    LINE_COLOR,
                    (0, i * SQUARE_SIZE),
                    (WIDTH, i * SQUARE_SIZE),
                    LINE_WIDTH)
        # draw vertical lines
        for i in range(0, BOARD_COLS + 1):
            if i % 3 == 0:
                pygame.draw.line(
                    self.screen,
                    LINE_COLOR,
                    (i * SQUARE_SIZE, 0),
                    (i * SQUARE_SIZE, HEIGHT),
                    # Made the HEIGHT divisible by 9 (693) under constants for a nicer looking board
                    BORDER_LINE_WIDTH)
            else:
                pygame.draw.line(
                    self.screen,
                    LINE_COLOR,
                    (i * SQUARE_SIZE, 0),
                    (i * SQUARE_SIZE, HEIGHT),
                    # Made the HEIGHT divisible by 9 (693) under constants for a nicer looking board
                    LINE_WIDTH)

    def draw_cell_numbers(self):
        for i in range(BOARD_COLS):
            for j in range(BOARD_ROWS):
                self.starting_cells[i][j].draw(self.screen)

    # used for marking the cell on the board at the selected cell (Tom)
    def select(self, row, col):

        return self.starting_cells[row][col]

    # finding the row and column of the board (Tom)
    def click(self, x, y):
        # instead of a value from 0 to 693, both give you 0-9
        row = y // SQUARE_SIZE
        col = x // SQUARE_SIZE
        if 0 <= row < BOARD_ROWS and 0 <= col < BOARD_ROWS:
            pygame.display.update()
            return tuple([row, col])  # returns the coordinates
        # Check if location of click is in button area
        elif (0 <= x <= WIDTH - 10) and (HEIGHT <= y <= HEIGHT + 80):
            location = (x, y)
            pygame.display.update()
            return location  # Return button area click location to check which button was clicked
        else:  # if outside the values
            return None  # returns None
        # self.cell = (x, y) # temporary attribute (corey 11/22) - removed/edited (Tom)

    def clear(self, cell):
        if cell.user_editable is True:
            cell.set_cell_value(0)
            cell.enter_value(cell.value)

    '''
    Added function to check if selected cell is editable.
    Returns False if cell was part of original board.
    '''

    def editable_cell(self, row, col):
        if self.starting_cells[row][col].value == 0:
            return True
        else:
            return False

    # Updated sketch function to see if it works - Jason
    def sketch(self, cell, value):
        if self.editable_cell(cell.row, cell.col):
            sketched_value = cell.set_sketched_value(value)
            return sketched_value
        '''
        #update cell object at selected cell (object with matching row and column)
        for cells in self.active_board:
            if (cells.row == self.selected_cell[0] and cells.col == self.selected_cell[1]):
                cells.set_sketched_value(value)
        '''

    # Updated to call cell new cell.enter_value function - Jason
    def place_number(self, cell, value):
        if cell.sketched is True:
            cell.set_cell_value(cell.sketched_value)
            cell.enter_value(cell.value)
        else:
            cell.set_cell_value(cell.value)
            cell.enter_value(cell.value)

        # do we need to check if the cell was empty (0) at game start?
        # Possibly - we can use editable_cell to check. - Jason
        # But if main function limits placing number to after sketching, we already check for validity at sketching

    def reset_to_original(self):
        # self.sketched_cells = self.starting_cells  # Set player updated cells to equal starting cells
        # self.starting_board = self.generated_board  # Set player updated board equal to initial board
        for rows in range(BOARD_ROWS):
            for cols in range(BOARD_COLS):
                self.starting_cells[rows][cols].value = self.starting_board[rows][cols]
                self.starting_cells[rows][cols].sketched_value = 0
                self.starting_cells[rows][cols].sketched = False

    def is_full(self):
        # look for any 0 in cell.value
        for rows in range(BOARD_ROWS):
            for cols in range(BOARD_COLS):
                if self.starting_cells[rows][cols].value == 0:
                    return False
        return True

    def update_board(self):  # Unsure what this method is supposed to be doing
        pass

    def find_empty(self):
        # loop through cell.value and find the first 0 and return its coordinates
        for row in range(BOARD_ROWS):
            for column in range(BOARD_COLS):
                if self.starting_cells[row][column] == 0:
                    return row, column
        # Do we want to return anything if there is no empty cells?

    def check_board(self):
        # loop through cell.value and compare to the "solution"
        for row in range(BOARD_ROWS):
            for column in range(BOARD_COLS):
                if self.starting_cells[row][column].value != self.solution_board[row][column]:
                    return False
        return True

    # using to play around with the game_over part of sudoku.py. Can be deleted if needed (Tom)
    def is_game_over(self):
        return self.is_full() and self.check_board()
