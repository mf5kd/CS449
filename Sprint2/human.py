from player import Player

# Class for the Human Player
# hold the symbol and color of the player
class Human(Player):
    def __init__(self, symbol, color):
        super().__init__(symbol, color)