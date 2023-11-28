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
        self.board = self.set_board()
        self.initial_cells = [
            [Cell(self.board[i][j], i, j, self.screen) for j in range(BOARD_COLS)]
            for i in range(BOARD_ROWS)
        ]

    def set_board(self): #new method to call SudokuGenerator
        self.removed_cells = 0 #holds int of # cells removed from solved board
        self.active_board = []  #holds a list of cell objects
        self.solved_board = []  #holds the solved board for comparison purposes # FIX ME
        if self.difficulty == 1: self.removed_cells = 30    #conditional to set removed cells
        elif self.difficulty == 2: self.removed_cells = 40
        elif self.difficulty == 3: self.removed_cells = 50
        self.s = SudokuGenerator(BOARD_ROWS, self.removed_cells)    #generate board
        self.s.fill_values()
        self.solved_board = self.s.get_board()
        # for index in range(len(self.s.board)):
            # self.solved_board.append(self.s.board[index]) #FIX ME: this definition is overwritten by remove_cells()
        print(self.solved_board)
        self.s.remove_cells()
        self.active_board = self.s.get_board() #get the starting board configuration
        print(self.active_board)
        # for row in range(BOARD_ROWS):   #populate list of cell objects
        #    for column in range(BOARD_COLS):
        #        self.active_board.append(Cell(self.generated_board[row][column], row, column,self.screen))
                # FIX ME: need to figure out what to put in "screen" attribute
        return self.active_board

    def draw(self): # draws the grids for the game (Tom)
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
                self.initial_cells[i][j].draw(self.screen)

    def select(self, row, col): # used for marking the cell on the board at the selected cell (Tom)
        self.selected_cell = (row, col)


    def click(self, x, y): # finding the row and column of the board (Tom)
        row = y // SQUARE_SIZE # instead of a value from 0 - 693, it gives you 0-9
        col = x // SQUARE_SIZE # instead of a value from 0 - 693, it gives you 0-9

        if 0 <= row < BOARD_ROWS and 0 <= col < BOARD_ROWS: # if the value is within the board paramenters
            pygame.display.update()
            return tuple([row, col]) # returns the coordinates
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

    def sketch(self, value):
        #update cell object at selected cell (object with matching row and column)
        for cells in self.active_board:
            if (cells.row == self.selected_cell[0] and cells.col == self.selected_cell[1]):
                cells.set_sketched_value(value)

    def place_number(self, value):
        for cells in self.active_board:
            if (cells.row == self.selected_cell[0] and cells.col == self.selected_cell[1]):
                cells.set_cell_value(value)

        #do we need to check if the cell was empty (0) at game start?

    def reset_to_original(self):
        #loop through initial board and set active board to equal values in cell class
        for row in range(9):
            for column in range(9):
                for cells in self.active_board:
                    if (cells.row == row and cells.col == column):
                        cells.set_cell_value(self.generated_board[row][column])

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
        for row in range(9):
            for column in range(9):
                for cells in self.active_board:
                    if(cells.row == row and cells.col == column and cells.value != self.solved_board[row][column]):
                        return False
        return True
