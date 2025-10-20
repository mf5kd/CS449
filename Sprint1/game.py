class Game:
    def __init__(self, blue_player, red_player, board_size, game_type):
        self.blue_player = blue_player
        self.red_player = red_player
        self.board_size = board_size
        self.current_player = blue_player
        self.game_type = game_type
        self.game_board = [[" " for x in range(self.board_size)] for x in range(self.board_size)]
        self.winner = None
        
    def change_player(self):
        if self.current_player == self.blue_player:
            self.current_player == self.red_player
            return self.red_player
        self.current_player = self.blue_player
        return self.blue_player
    
    def player_move(self, row, column):
        if self.game_board[row][column] == " " and not self.winner:
            self.game_board[row][column] == self.current_player.symbol
            return True
        return False
    
    def check_win(self):
        pass
    
    def check_draw(self):
        pass
    
    def get_current_player(self):
        return self.current_player