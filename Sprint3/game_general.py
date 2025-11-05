from game import Game

# Class for the general Game 
# inherits from game
class General(Game):
    def __init__(self, blue_player, red_player, board_size):
        super().__init__(blue_player, red_player, board_size)
        self.blue_score = 0
        self.red_score = 0

        # stores the point conditions 
        # as what counts as a point
        self.directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

    # Overloaded function
    def player_move(self, row, column):
        move_was_valid = super().player_move(row, column)
        
        if move_was_valid:
            self.update_score_from_move(row, column)
            
        return move_was_valid
      
    # update the current score of the players  
    def update_score_from_move(self, row, column):
        symbol_placed = self.game_board[row][column]
        points_scored = 0

        if symbol_placed == 'O':
            for d_row, d_column in self.directions[:4]:
                row_one, column_one = row + d_row, column + d_column
                row_two, column_two = row - d_row, column - d_column

                if (0 <= row_one < self.board_size and 0 <= column_one < self.board_size and
                    0 <= row_two < self.board_size and 0 <= column_two < self.board_size):

                    if (self.game_board[row_one][column_one] == 'S' and
                        self.game_board[row_two][column_two] == 'S'):
                        points_scored += 1
                        
        elif symbol_placed == 'S':
            for d_row, d_column in self.directions:
                row_o, column_o = row + d_row, column + d_column
                row_s, column_s = row + 2*d_row, column + 2*d_column

                if (0 <= row_o < self.board_size and 0 <= column_o < self.board_size and
                    0 <= row_s < self.board_size and 0 <= column_s < self.board_size):

                    if (self.game_board[row_o][column_o] == 'O' and
                        self.game_board[row_s][column_s] == 'S'):
                        points_scored += 1


        if self.current_player == self.blue_player:
            self.blue_score += points_scored
        else:
            self.red_score += points_scored   
        
    def check_draw(self):
        is_board_full = super().check_draw()

        if is_board_full:
            if self.blue_score > self.red_score:
                self.winner = self.blue_player
            elif self.red_score > self.blue_score:
                self.winner = self.red_player
            else:
                self.winner = None
            return True
        return False
    
    def check_win(self):
        return False

    def get_blue_score(self):
        return self.blue_score

    def get_red_score(self):
        return self.red_score
