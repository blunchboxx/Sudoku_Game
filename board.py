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
        pass

    def clear(self): #IN WORK: Corey 11/20/23
        #check if cell was empty at game start
            #set_cell_value(0) (cell class) #update to tell specify which cell
        pass

    def sketch(self, value): #IN WORK: Corey 11/20/23


        #update once draw() is finished
        pass

    def place_number(self, value): #IN WORK: Corey 11/20/23
        # set_cell_value(value) (cell class) #UPDATE to tell specify which cell

        pass

    def reset_to_original(self): #IN WORK: Corey 11/20/23
        #for loop that goes through original 2-d array and assigns corresponding values
        pass

    def is_full(self): #IN WORK: Corey 11/20/23
        #for loop that steps through 2-d array and checks for 0's
        pass

    def update_board(self): #IN WORK: Corey 11/20/23
        pass

    def find_empty(self): #IN WORK: Corey 11/20/23
        #for loop through current aray and looks for 0
        pass

    def check_board(self): #IN WORK: Corey 11/20/23
        #for loop that compares each element to corresponding element in solution 2-d array
        pass
