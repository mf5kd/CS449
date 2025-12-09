# Main Class of the player 
# Human and computer inherit from this class
class Player:
    def __init__(self, symbol, color):
        # symbol will be either "s" or "o"
        if symbol == 1:
            self.symbol = "S"
        else:
            self.symbol = "O"
        # color will be red or blue
        self.color = color
    
    # getter and setter
    def get_symbol(self):
        return self.symbol
    
    def set_symbol(self, symbol):
        if symbol == 1:
            self.symbol = "S"
        else:
            self.symbol = "O"
    
    def get_color(self):
        return self.color
    