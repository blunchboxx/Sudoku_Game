class Board:
    pass

    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty

    def draw(self):
        pass

    def select(self, row, col):
        pass

    def click(self, x, y):
        self.cell = (x,y) #temporary attribute (corey 11/22)

    def clear(self):
        #check if cell was empty at game start
        # Update once cell is complete to set_cell_value(0) (cell class)
#        if self.board_removed_test[self.cell[0]][self.cell[1]] != 0:    #check if cell was filled in at game start
#            print("Cannot clear cell")
#        else:
#            self.board_active_test[self.cell[0]][self.cell[1]] = 0
        pass

    def sketch(self, value):
        # update once draw() is finished
        pass

    def place_number(self, value):
        # Update once proper board list is written: set_cell_value(value) (cell class)
#        self.board_active_test[self.cell[0]][self.cell[1]] = value

        #do we need to check if the cell was empty (0) at game start?
        pass

    def reset_to_original(self):
        # for loop that goes through original 2-d array and assigns corresponding values
#        for row in range(9):
#            for column in range(9):
#                self.board_active_test[row][column] = self.board_removed_test[row][column]
        pass

    def is_full(self):
        #for loop that steps through 2-d array and checks for 0's
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
