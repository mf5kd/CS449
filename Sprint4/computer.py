import os
import random
import re
import google.generativeai as genai
from player import Player

class Computer(Player):
    def __init__(self, symbol, color):
        super().__init__(symbol, color)

        self.api_key = os.getenv("GOOGLE_API_KEY")
        self.model = None
        
        if self.api_key:
            try:
                genai.configure(api_key=self.api_key)
                self.model = genai.GenerativeModel('gemini-2.0-flash')
            except Exception as e:
                print(f"Error configuring Google API: {e}")
        else:
            print("Warning: GOOGLE_API_KEY not found. Computer will play randomly.")

    def make_move(self, game_board, board_size, game_mode):
        if self.model:
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
            f"Your current symbol to place is: '{self.symbol}'.\n\n"
            f"Current Board State (Empty spots are '_'):\n{board_str}\n"
            "Rules:\n"
            "- You must select an empty spot (marked as '_').\n"
            "- You want to form the sequence 'S-O-S' orthogonally or diagonally.\n"
            "- Return ONLY the row and column number as a comma-separated pair (e.g., '0, 2').\n"
            "- Rows and Columns are 0-indexed.\n"
            "Move:"
        )


        response = self.model.generate_content(prompt)
        text_response = response.text.strip()
        print(f"LLM Raw Response: {text_response}")

        match = re.search(r"(\d+)\s*,\s*(\d+)", text_response)
        if match:
            row, col = int(match.group(1)), int(match.group(2))
            

            if 0 <= row < board_size and 0 <= col < board_size:
                if game_board[row][col] == " ":
                    return row, col
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
            return random.choice(empty_spots)
        return -1, -1  