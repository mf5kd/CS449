class Game:
    def __init__(self, blue_player, red_player, board_size):
        self.blue_player = blue_player
        self.red_player = red_player
        self.board_size = board_size
        self.current_player = blue_player
        self.game_board = [[" " for x in range(self.board_size)] for x in range(self.board_size)]
        self.winner = None
        
    def change_player(self):
        if self.current_player == self.blue_player:
            self.current_player = self.red_player
            return self.red_player
        else:
            self.current_player = self.blue_player
            return self.blue_player
    
    def player_move(self, row, column):
        if self.game_board[row][column] == " " and not self.winner:
            self.game_board[row][column] = self.current_player.get_symbol()
            return True
        return False
    
    def check_win(self):
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1) 
        ]

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
                                return True
        return False
    
    def check_draw(self):
        if self.winner:
            return False

        for row in range(self.board_size):
            for column in range(self.board_size):
                if self.game_board[row][column] == " ":
                    return False
        return True
    
    def get_current_player(self):
        return self.current_player
    
    def get_winner(self):
        return self.winner