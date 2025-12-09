import unittest
import tkinter as tk
from unittest.mock import MagicMock, patch 
from gui import SOSGUI
from game import Game
from game_general import General
from human import Human
from computer import Computer
from controller import GameController

class TestGameLogic(unittest.TestCase):
    def setUp(self):
        self.blue_player = Human(1, "blue") # Starts with 'S'
        self.red_player = Human(2, "red")   # Starts with 'O'
        
        # Create root and GUI for each test (without showing window)
        self.root = tk.Tk()
        self.root.withdraw()  # hide window during tests
        self.controller = GameController()
        self.app = SOSGUI(self.root, self.controller)
        self.controller.set_view(self.app)

    def tearDown(self):
        self.root.destroy()

    # --- AC 1.1 Valid board size entered ---
    def test_valid_board_size_starts_game(self):
        self.app.board_size_entry.insert(0, "5")
        self.app.default_game_mode.set(1)  # Simple game
        self.controller.start_new_game()
        self.assertIsInstance(self.controller.current_game, Game)
        self.assertEqual(self.app.board_size, 5)
        self.assertEqual(len(self.app.game_spaces), 5)
        self.assertEqual(len(self.app.game_spaces[0]), 5)

    # --- AC 1.2 Invalid board size entered (<3) ---
    def test_invalid_board_size_shows_error(self):
        self.app.board_size_entry.insert(0, "2")
        # Mock the messagebox so we don't show an actual popup
        called = {}
        def mock_error(title, message):
            called["title"] = title
            called["message"] = message
        from tkinter import messagebox
        messagebox.showerror = mock_error

        self.controller.start_new_game()
        self.assertIn("title", called)
        self.assertIn("Board", called["message"])

    # --- AC 2.1 Simple game chosen ---
    def test_simple_game_mode_creates_game(self):
        self.app.board_size_entry.insert(0, "3")
        self.app.default_game_mode.set(1)
        self.controller.start_new_game()
        self.assertIsInstance(self.controller.current_game, Game)
        self.assertNotIsInstance(self.controller.current_game, General)

    # --- AC 2.2 General game chosen ---
    def test_general_game_mode_creates_general_game(self):
        self.app.board_size_entry.insert(0, "4")
        self.app.default_game_mode.set(2)
        self.controller.start_new_game()
        self.assertIsInstance(self.controller.current_game, General)

    # US 3: Start a new game
    # AC 3.1: A new game starts
    def test_ac_3_1_start_new_game(self):
        """Test the initial state of a new game."""
        simple_game = Game(self.blue_player, self.red_player, 3)
        self.assertEqual(simple_game.get_current_player(), self.blue_player)
        self.assertIsNone(simple_game.get_winner())
        # Check for empty board
        self.assertTrue(all(cell == " " for row in simple_game.game_board for cell in row))

        general_game = General(self.blue_player, self.red_player, 4)
        self.assertEqual(general_game.get_blue_score(), 0)
        self.assertEqual(general_game.get_red_score(), 0)
        self.assertTrue(all(cell == " " for row in general_game.game_board for cell in row))

    # US 4: Make a move in a simple game
    # AC 4.1: User makes a valid move
    def test_ac_4_1_simple_game_valid_move(self):
        """Test a valid move in a simple game."""
        game = Game(self.blue_player, self.red_player, 3)
        self.blue_player.set_symbol(1) # 'S'
        
        move_successful = game.player_move(1, 1)
        
        self.assertTrue(move_successful)
        self.assertEqual(game.game_board[1][1], 'S')
        
    # AC 4.2: User makes an invalid move
    def test_ac_4_2_simple_game_invalid_move(self):
        """Test an invalid move (on an occupied space) in a simple game."""
        game = Game(self.blue_player, self.red_player, 3)
        game.player_move(1, 1) # Blue player moves
        game.change_player()   # Red player's turn
        
        move_successful = game.player_move(1, 1) # Red player tries same spot
        
        self.assertFalse(move_successful)
        self.assertEqual(game.game_board[1][1], self.blue_player.get_symbol())

    # US 5: A simple game is over
    # AC 5.1: An SOS is made on the board (win)
    def test_ac_5_1_simple_game_win(self):
        """Test for a win condition in a simple game."""
        game = Game(self.blue_player, self.red_player, 3)
        # Setup board: S _ S
        game.game_board[0][0] = 'S'
        game.game_board[0][2] = 'S'
        
        # Current player is blue, who will place an 'O'
        self.blue_player.set_symbol(2) # 'O'
        game.player_move(0, 1) # Blue player places 'O' in the middle
        
        self.assertTrue(game.check_win())
        self.assertEqual(game.get_winner(), self.blue_player)

    # AC 5.2: The Board is full (draw)
    def test_ac_5_2_simple_game_draw(self):
        """Test for a draw condition in a simple game."""
        game = Game(self.blue_player, self.red_player, 3)
        # Fill the board with a non-winning pattern
        game.game_board = [
            ['S', 'S', 'O'],
            ['O', 'O', 'S'],
            ['S', 'O', 'S']
        ]
        self.assertTrue(game.check_draw())
        self.assertIsNone(game.get_winner())

    # US 6: Make a move in a general game
    # AC 6.1: Player places a letter on the board
    def test_ac_6_1_general_game_valid_move(self):
        """Test that a letter is placed correctly in a general game."""
        game = General(self.blue_player, self.red_player, 3)
        self.blue_player.set_symbol(1) # 'S'
        
        game.player_move(0, 0)
        self.assertEqual(game.game_board[0][0], 'S')
        self.assertEqual(game.get_blue_score(), 0) # No points scored yet

    # AC 6.2: Player creates an SOS sequence (scores point)
    def test_ac_6_2_general_game_scores_point_with_o(self):
        """Test that a player scores a point by placing an 'O'."""
        game = General(self.blue_player, self.red_player, 3)
        game.game_board[0][0] = 'S'
        game.game_board[0][2] = 'S'
        
        self.blue_player.set_symbol(2) # 'O'
        game.player_move(0, 1) # Blue player places 'O' to score
        
        self.assertEqual(game.get_blue_score(), 1)
        self.assertEqual(game.get_red_score(), 0)

    def test_ac_6_2_general_game_scores_point_with_s(self):
        """Test that a player scores a point by placing an 'S'."""
        game = General(self.blue_player, self.red_player, 3)
        game.game_board[0][1] = 'O'
        game.game_board[0][2] = 'S'
        
        self.blue_player.set_symbol(1) # 'S'
        game.player_move(0, 0) # Blue player places 'S' to score
        
        self.assertEqual(game.get_blue_score(), 1)

    # AC 6.3: Player does not create an SOS sequence
    def test_ac_6_3_general_game_no_score(self):
        """Test that a move not creating an SOS results in no score change."""
        game = General(self.blue_player, self.red_player, 3)
        game.player_move(1, 1)
        self.assertEqual(game.get_blue_score(), 0)
        self.assertEqual(game.get_red_score(), 0)

    # US 7: A general game is over
    # AC 7.1: Board is completely filled
    def test_ac_7_1_general_game_ends_when_full(self):
        """Test that the game ends when the board is full."""
        game = General(self.blue_player, self.red_player, 3)
        game.game_board = [
            ['S', 'O', 'S'],
            ['S', 'S', 'O'],
            ['O', 'O', 'S']
        ]
        # Simulate a final move that scores for blue
        game.blue_score = 1
        game.red_score = 0
        self.assertTrue(game.check_draw())
    
    # AC 7.2: One player has more SOS sequences (wins)
    def test_ac_7_2_general_game_winner_highest_score(self):
        """Test that the player with the higher score wins."""
        game = General(self.blue_player, self.red_player, 3)
        game.game_board = [['S'] * 3 for _ in range(3)] # Fill the board
        game.blue_score = 3
        game.red_score = 1
        
        game.check_draw() # This method also sets the winner in General game
        self.assertEqual(game.get_winner(), self.blue_player)

    # AC 7.3: Both players have the same score (draw)
    def test_ac_7_3_general_game_draw(self):
        """Test that the game is a draw if scores are equal."""
        game = General(self.blue_player, self.red_player, 3)
        game.game_board = [['S'] * 3 for _ in range(3)] # Fill the board
        game.blue_score = 2
        game.red_score = 2

        game.check_draw()
        self.assertIsNone(game.get_winner())

class TestComputerPlayer(unittest.TestCase):
    def setUp(self):
        # Initialize computer player
        self.computer = Computer(2, "red")
        self.board_size = 3
        # Create empty 3x3 board
        self.empty_board = [[" " for _ in range(3)] for _ in range(3)]

    # Random Move (No API / Fallback)
    def test_computer_fallback_random_move(self):
        # Force model to None to simulate missing API key or init failure
        self.computer.model = None 
        
        row, col, symbol = self.computer.make_move(self.empty_board, self.board_size, 1)
        
        # Check bounds
        self.assertTrue(0 <= row < self.board_size, "Row is out of bounds")
        self.assertTrue(0 <= col < self.board_size, "Column is out of bounds")
        # Check symbol
        self.assertIn(symbol, ['S', 'O'], "Symbol must be S or O")

    # Valid LLM Move
    def test_computer_llm_valid_move(self):
        # Create a Mock model
        mock_model = MagicMock()
        mock_response = MagicMock()
        
        # Simulate LLM returning "1, 1, S"
        mock_response.text = "1, 1, S" 
        mock_model.generate_content.return_value = mock_response
        
        # Inject mock model into computer
        self.computer.model = mock_model
        
        row, col, symbol = self.computer.make_move(self.empty_board, self.board_size, 1)
        
        self.assertEqual(row, 1)
        self.assertEqual(col, 1)
        self.assertEqual(symbol, 'S')

    # LLM Error/Crash Recovery
    def test_computer_recovers_from_llm_error(self):
        mock_model = MagicMock()
        # Make the generate_content method raise an error
        mock_model.generate_content.side_effect = Exception("API Connection Failed")
        
        self.computer.model = mock_model
        
        # Attempt move - should not crash
        row, col, symbol = self.computer.make_move(self.empty_board, self.board_size, 1)
        
        # Should return a valid random move instead
        self.assertTrue(0 <= row < self.board_size)
        self.assertIn(symbol, ['S', 'O'])

if __name__ == '__main__':
    unittest.main()
