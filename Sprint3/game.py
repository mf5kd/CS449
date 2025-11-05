# Class for the simple game 
# General inherits from this class
import re


class Game:
    # class takes two players and the size of the board
    def __init__(self, blue_player, red_player, board_size):
        self.blue_player = blue_player
        self.red_player = red_player
        self.board_size = board_size
        self.current_player = blue_player
        
        self.game_board = [[" " for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.winner = None
        # holds the the location of the wining SOS
        self.winning_coords = []

    # changes the current player
    def change_player(self):
        if self.current_player == self.blue_player:
            self.current_player = self.red_player
            return self.red_player
        else:
            self.current_player = self.blue_player
            return self.blue_player
    
    # get the row and column where the player clicked
    # stores the location and symbol of the move
    def player_move(self, row, column):
        if self.game_board[row][column] == " " and not self.winner:
            self.game_board[row][column] = self.current_player.get_symbol()
            return True
        return False
    
    # checks if the game has been won 
    def check_win(self):
        # has the posible combimation of how to win horizontal, vertical, diagonal
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1) 
        ]

        # loops that check the board for a win
        for row in range(self.board_size):
            for column in range(self.board_size):

                if self.game_board[row][column] == 'O':
                    for d_row, d_column in directions[:4]:
                        row_one, column_one = row + d_row, column + d_column
                        row_two, column_two = row - d_row, column - d_column

                        if (0 <= row_one < self.board_size and 0 <= column_one < self.board_size and
                            0 <= row_two < self.board_size and 0 <= column_two < self.board_size):

                            if (self.game_board[row_one][column_one] == 'S' and
                                self.game_board[row_two][column_two] == 'S'):

                                self.winner = self.current_player
                                
                                self.winning_coords = [
                                    (row_one, column_one),
                                    (row, column),
                                    (row_two, column_two)
                                ]

                                return True # if the is a win 
        return False # if there is no win
    
    # check is no one won
    def check_draw(self):
        # if there is a winner choose
        # it is not a draw
        if self.winner:
            return False
        
        # loops that check for draw
        for row in range(self.board_size):
            for column in range(self.board_size):
                if self.game_board[row][column] == " ":
                    return False # if the is a draw
        return True # if there is no draw
    
    # getters
    def get_current_player(self):
        return self.current_player
    
    def get_winner(self):
        return self.winner

    def get_winning_coords(self):
        return self.winning_coords
    
