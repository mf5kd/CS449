from game import Game
from game_general import General
from human import Human
from computer import Computer

class GameController:
    def __init__(self):
        self.view = None
        self.current_game = None
        self.blue_player = None
        self.red_player = None

    def set_view(self, view):
        self.view = view

    def start_new_game(self):
        try:
            board_size = self.view.get_board_size()
            if board_size < 3:
                raise ValueError("Board size must be 3 or greater.")
            
            game_mode = self.view.get_game_mode()
            
            blue_player_type = self.view.get_blue_player_type()
            red_player_type = self.view.get_red_player_type()

            if blue_player_type == 1:
                self.blue_player = Human(1, "blue")
            else:
                self.blue_player = Computer(1, "blue")

            if red_player_type == 1:
                self.red_player = Human(2, "red")
            else:
                self.red_player = Computer(2, "red")

            if game_mode == 1:
                self.current_game = Game(self.blue_player, self.red_player, board_size)
            else:
                self.current_game = General(self.blue_player, self.red_player, board_size)

            self.view.reset_board(board_size)
            self.view.set_turn_label(
                f"IT IS {self.current_game.get_current_player().get_color().upper()} TURN"
            )

            if isinstance(self.current_game.get_current_player(), Computer):
                    self.handle_computer_turn()
                
        except ValueError as e:
            self.view.show_error(f"Invalid Input: {e}")

    def handle_board_click(self, row, column):
        if not self.current_game:
            return
            
        if not isinstance(self.current_game.get_current_player(), Human):
            return

        blue_letter = self.view.get_blue_letter_type()
        red_letter = self.view.get_red_letter_type()

        self.blue_player.set_symbol(blue_letter)
        self.red_player.set_symbol(red_letter)

        move_made = self.current_game.player_move(row, column)
        
        if not move_made:
            return

        self._check_and_update_game_state(row, column)
        
    def end_game(self, end_type):
        self.view.disable_board()
        if end_type == "WINNER":
            self.view.set_turn_label(
                f"{self.current_game.get_winner().get_color().upper()} IS THE WINNER"
            )
        elif end_type == "DRAW":
            self.view.set_turn_label("THE GAME IS A DRAW")
        else:
            self.view.set_turn_label("GAME ENDED DUE TO ERROR (COMPUTER INVALID MOVE)")


    def handle_computer_turn(self):
        self.view.disable_board()
        self.view.set_turn_label("COMPUTER IS THINKING...")
        self.view.root.update()

        current_player = self.current_game.get_current_player()
        game_mode = self.view.get_game_mode()
        
        if current_player == self.blue_player:
            symbol_type = self.view.get_blue_letter_type()
        else:
            symbol_type = self.view.get_red_letter_type()
        current_player.set_symbol(symbol_type)

        row, column = current_player.make_move(
            self.current_game.game_board, 
            self.current_game.board_size,
            game_mode
        )

        move_made = self.current_game.player_move(row, column)
        
        if move_made:
            self._check_and_update_game_state(row, column)
        else:
            print(f"Computer made an invalid move: ({row}, {column})")
            self.end_game("ERROR")

    def _check_and_update_game_state(self, row, column):
        game_mode = self.view.get_game_mode()
        is_win = self.current_game.check_win()
        is_draw = self.current_game.check_draw()

        self.view.update_board_display(is_win, game_mode)
        
        if is_win:
            self.end_game("WINNER")
            return
        elif is_draw:
            winner = self.current_game.get_winner()
            if game_mode == 1 or winner is None:
                self.end_game("DRAW")
            else:
                self.end_game("WINNER")
            return

        self.current_game.change_player()
        
        if isinstance(self.current_game.get_current_player(), Computer):
            self.view.root.after(500, self.handle_computer_turn)
        else:
            self.view.set_turn_label(
                f"IT IS {self.current_game.get_current_player().get_color().upper()} TURN"
            )
            self.view.enable_board()