class Player:
    def __init__(self, symbol, color):
        # symbol will be either "s" or "o" 
        self.symbol = symbol
        # color will be red or blue
        self.color = color
        
    def get_symbol(self):
        return self.symbol
    
    def get_color(self):
        return self.color