import os
import random
import re
from google import genai
from google.genai import types
from player import Player

class Computer(Player):
    def __init__(self, symbol, color):
        super().__init__(symbol, color)

        self.api_key = os.getenv("GOOGLE_API_KEY")
        self.client = None
        
        if self.api_key:
            try:
                self.client = genai.Client(api_key = self.api_key)
            except Exception as e:
                print(f"Error configuring Google API: {e}")
        else:
            print("Warning: GOOGLE_API_KEY not found. Computer will play randomly.")

    def make_move(self, game_board, board_size, game_mode):
        if self.client:
            try:
                return self._get_llm_move(game_board, board_size, game_mode)
            except Exception as e:
                print(f"LLM Error: {e}. Falling back to random move.")
        
        return self._get_random_move(game_board, board_size)

    def _get_llm_move(self, game_board, board_size, game_mode):
        board_str = ""
        for row in game_board:
            row_str = " | ".join([cell if cell.strip() != "" else "_" for cell in row])
            board_str += f"| {row_str} |\n"


        mode_str = "Simple Game (First to complete SOS wins)" if game_mode == 1 else "General Game (Most SOSs wins)"
        
        prompt = (
            f"You are playing the board game SOS. You are the {self.color} player.\n"
            f"The board size is {board_size}x{board_size}.\n"
            f"Game Mode: {mode_str}.\n"
            f"Current Board State (Empty spots are '_'):\n{board_str}\n"
            "Rules:\n"
            "- You must select an empty spot (marked as '_').\n"
            "- You must CHOOSE to place either 'S' or 'O'.\n"
            "- You want to form the sequence 'S-O-S' orthogonally or diagonally.\n"
            "- Return ONLY the row, column, and symbol separated by commas (e.g., '0, 2, S').\n"
            "- Rows and Columns are 0-indexed.\n"
            "Move:"
        )


        response = self.client.models.generate_content(
            model = "gemini-2.5-flash-lite",
            contents = prompt,
            config = types.GenerateContentConfig(
                temperature = 0.0
            )
        )

        text_response = response.text.strip()
        print(f"LLM Raw Response: {text_response}")

        match = re.search(r"(\d+)\s*,\s*(\d+)\s*,\s*([sSoO])", text_response)
        if match:
            row = int(match.group(1))
            col = int(match.group(2))
            symbol = match.group(3).upper() # Ensure it is uppercase

            if 0 <= row < board_size and 0 <= col < board_size:
                if game_board[row][col] == " ":
                    return row, col, symbol
                else:
                    print(f"LLM suggested occupied spot: {row}, {col}")
            else:
                print(f"LLM suggested out-of-bounds: {row}, {col}")
        
        raise ValueError("Invalid response from LLM")

    def _get_random_move(self, game_board, board_size):
        empty_spots = []
        for r in range(board_size):
            for c in range(board_size):
                if game_board[r][c] == " ":
                    empty_spots.append((r, c))
        
        if empty_spots:
            r, c = random.choice(empty_spots)
            symbol = random.choice(['S', 'O'])
            return r, c, symbol
            
        return -1, -1, 'S'
