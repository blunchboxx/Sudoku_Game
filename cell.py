class Cell:
    pass

    def __init__(self, value, row, col, screen):  # Initialize Cell variables
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen

    def set_cell_value(self, value):  # Setter for cell value
        self.value = value

    def set_sketched_value(self, value):  # Setter for cell's sketched value
        pass

    def draw(self):  # Draws cell with value inside it

        if self.value == 0:  # If cell value is zero, display nothing inside cell
            # FixMe: Define empty displayed cell if value is still zero
            pass
        elif self.value > 0:
            # FixMe: Draw cell and current value
            pass

        pass
