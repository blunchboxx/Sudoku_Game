import math, random

"""
This was adapted from a GeeksforGeeks article "Program for Sudoku Generator" by Aarti_Rathi and Ankur Trisal
https://www.geeksforgeeks.org/program-sudoku-generator/

"""


class SudokuGenerator:
    '''
    Create a sudoku board - initialize class variables and set up the 2D board
    This should initialize:
    self.row_length		- the length of each row
    self.removed_cells	- the total number of cells to be removed
    self.board			- a 2D list of ints to represent the board
    self.box_length		- the square root of row_length

    Parameters:
    row_length is the number of rows/columns of the board (always 9 for this project)
    removed_cells is an integer value - the number of cells to be removed

    Return:
    None
    '''

    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.box_length = int(math.sqrt(self.row_length))
        self.board = []          #LINES 31-34 NEW 11/15/23 - Corey Cavalli
        for row in range(9):
            self.board.append([])
            for column in range(9): self.board[row].append(0)

    '''
    Returns a 2D python list of numbers which represents the board

    Parameters: None
    Return: list[list]
    '''

    def get_board(self):
        return self.board

    '''
    Displays the board to the console
    This is not strictly required, but it may be useful for debugging purposes

    Parameters: None
    Return: None
    '''

    def print_board(self):

        for i in range(0, len(self.board)):
            print(f'{self.board[i]}\n')

    '''
    Determines if num is contained in the specified row (horizontal) of the board
    If num is already in the specified row, return False. Otherwise, return True

    Parameters:
    row is the index of the row we are checking
    num is the value we are looking for in the row
    
    Return: boolean
    '''

    def valid_in_row(self, row, num):

        if num in self.board[row]:
            return False
        else:
            return True

    '''
    Determines if num is contained in the specified column (vertical) of the board
    If num is already in the specified col, return False. Otherwise, return True

    Parameters:
    col is the index of the column we are checking
    num is the value we are looking for in the column
    
    Return: boolean
    '''

    def valid_in_col(self, col, num):

        for i in range(0, self.row_length):
            if num == self.board[i][col]:
                return False

        return True

    '''
    Determines if num is contained in the 3x3 box specified on the board
    If num is in the specified box starting at (row_start, col_start), return False.
    Otherwise, return True

    Parameters:
    row_start and col_start are the starting indices of the box to check
    i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)
    num is the value we are looking for in the box

    Return: boolean
    '''

    def valid_in_box(self, row_start, col_start, num):

        for row in range(row_start, row_start + self.box_length):
            for col in range(col_start, col_start + self.box_length):
                if num == self.board[row][col]:
                    return False

        return True

    '''
    Determines if it is valid to enter num at (row, col) in the board
    This is done by checking that num is unused in the appropriate, row, column, and box

    Parameters:
    row and col are the row index and col index of the cell to check in the board
    num is the value to test if it is safe to enter in this cell

    Return: boolean
    '''

    def is_valid(self, row, col, num):

        # Determine Row Start value
        if row < 3:
            row_start = 0

        elif 3 <= row < 6:
            row_start = 3

        elif 6 <= row < 10:
            row_start = 6

        # Determine Col Start Value
        if col < 3:
            col_start = 0

        elif 3 <= col < 6:
            col_start = 3

        elif 6 <= col < 10:
            col_start = 6

        if (self.valid_in_row(row, num) == self.valid_in_col(col, num) ==
                self.valid_in_box(row_start, col_start, num) == True):
            return True

        return False

    '''
    Determines if value has been used in box yet during initial board generation'

    Parameters:
    row_start and col_start are the indices of the box we are checking
    value is the number we are checking if it is in the desired row/column location

    Returns: Boolean
    '''

    def unused_in_box(self, row_start, col_start, value):

        for row in range(row_start, row_start + self.box_length):
            for col in range(col_start, col_start + self.box_length):
                if self.board[row][col] == value:
                    return False

        return True

    '''
    Fills the specified 3x3 box with values
    For each position, generates a random digit which has not yet been used in the box

    Parameters:
    row_start and col_start are the starting indices of the box to check
    i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)

    Return: None
    '''

    def fill_box(self, row_start, col_start):

        for row in range(row_start, row_start + self.box_length):
            for col in range(col_start, col_start + self.box_length):
                    next_value = random.randint(1, 9)

                    while self.unused_in_box(row_start, col_start, next_value) is False:
                        next_value = random.randint(1, 9)

                    self.board[row][col] = next_value

    '''
    Fills the three boxes along the main diagonal of the board
    These are the boxes which start at (0,0), (3,3), and (6,6)

    Parameters: None
    Return: None
    '''

    def fill_diagonal(self):
        self.fill_box(0, 0)
        self.fill_box(3, 3)
        self.fill_box(6, 6)

    '''
    DO NOT CHANGE
    Provided for students
    Fills the remaining cells of the board
    Should be called after the diagonal boxes have been filled
    
    Parameters:
    row, col specify the coordinates of the first empty (0) cell

    Return:
    boolean (whether or not we could solve the board)
    '''

    def fill_remaining(self, row, col):
        if col >= self.row_length and row < self.row_length - 1:
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    '''
    DO NOT CHANGE
    Provided for students
    Constructs a solution by calling fill_diagonal and fill_remaining

    Parameters: None
    Return: None
    '''

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    '''
    Removes the appropriate number of cells from the board
    This is done by setting some values to 0
    Should be called after the entire solution has been constructed
    i.e. after fill_values has been called
    
    NOTE: Be careful not to 'remove' the same cell multiple times
    i.e. if a cell is already 0, it cannot be removed again

    Parameters: None
    Return: None
    '''

    def remove_cells(self):

        removed_cell_coordinates = []
        removed_count = 0

        while removed_count < self.removed_cells:

            rand_col = random.randint(0, 8)
            rand_row = random.randint(0, 8)

            if self.board[rand_row][rand_col] != 0:
                self.board[rand_row][rand_col] = 0
                removed_count += 1

'''
DO NOT CHANGE
Provided for students
Given a number of rows and number of cells to remove, this function:
1. creates a SudokuGenerator
2. fills its values and saves this as the solved state
3. removes the appropriate number of cells
4. returns the representative 2D Python Lists of the board and solution

Parameters:
size is the number of rows/columns of the board (9 for this project)
removed is the number of cells to clear (set to 0)

Return: list[list] (a 2D Python list to represent the board)
'''


def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board
