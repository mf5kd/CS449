import tkinter as tk
from tkinter import messagebox

class SOSGUI:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.board_size_entry = None
        self.board_frame = None
        self.current_turn_label = None
        
        # holds board size
        # holds the button of the game board in a list of list of buttons
        self.board_size = 3
        self.game_spaces = [[None for _ in range(self.board_size)] for _ in range(self.board_size)]
        
        # has the values for what gamemode(simple, general) is choose
        # also has the of blue and red players type(human, computer) and there letter(S, O)
        self.default_game_mode = tk.IntVar()
        self.blue_player_type = tk.IntVar()
        self.blue_letter_type = tk.IntVar()
        self.red_player_type = tk.IntVar()
        self.red_letter_type = tk.IntVar()

        
        self.create_widgets()
        
    def create_top_widgets(self, main_frame):
        # frame that holds the check buttons to choose between Simple game or General Game and there labels
        top_frame = tk.Frame(main_frame, border=1, borderwidth=10, relief="groove")
        top_frame.pack(side="top", fill="x")
        
        game_type_label = tk.Label(top_frame, text="SOS", border=1, relief="solid", font=("TkDefaultFont", 20) )
        game_type_label.pack(side="left")
        
        self.default_game_mode.set(1)
        
        simple_game_radio_button = tk.Radiobutton(top_frame, text="Simple Game", value=1, variable=self.default_game_mode)
        simple_game_radio_button.pack(side="left")

        general_game_radio_button = tk.Radiobutton(top_frame, text="General Game", value=2, variable=self.default_game_mode)
        general_game_radio_button.pack(side="left")
        
        board_size_frame = tk.Frame(top_frame)
        board_size_frame.pack(side="right", fill="x")

        board_size_label = tk.Label(board_size_frame, text="Board Size")
        board_size_label.pack(side="left")

        self.board_size_entry = tk.Entry(board_size_frame, width=2, border=5, relief="solid", font=("TkDefaultFont", 15))
        self.board_size_entry.pack(side="left")

    def create_left_widgets(self, main_frame):
        # frame that hold things to the left
        # holds that check Radio button for where blue is a human or computer
        # what letter they are placing
        left_frame = tk.Frame(main_frame, border=1, borderwidth=10, relief="groove")
        left_frame.pack(side="left", fill="y")

        blue_player_label = tk.Label(left_frame, text="Blue Player")
        blue_player_label.pack()
        
        self.blue_player_type.set(1)
        self.blue_letter_type.set(1)

        blue_human = tk.Radiobutton(left_frame, text="Human", value=1, variable=self.blue_player_type)
        blue_human.pack()
        blue_s = tk.Radiobutton(left_frame, text="S", value=1, variable=self.blue_letter_type)
        blue_s.pack()
        blue_o = tk.Radiobutton(left_frame, text="O", value=2, variable=self.blue_letter_type)
        blue_o.pack()
        blue_computer = tk.Radiobutton(left_frame, text="Computer", value=2, variable=self.blue_player_type)
        blue_computer.pack()
        
    def create_right_widgets(self, main_frame):
        # frame that hold things to the right
        # holds that check buttons for where red is a human or computer
        # what letter they are placing
        right_frame = tk.Frame(main_frame, border=1, borderwidth=10, relief="groove")
        right_frame.pack(side="right", fill="y")

        red_player_label = tk.Label(right_frame, text="Red Player")
        red_player_label.pack()

        self.red_player_type.set(1)
        self.red_letter_type.set(2)

        red_human = tk.Radiobutton(right_frame, text="Human", value=1, variable=self.red_player_type)
        red_human.pack()
        red_s = tk.Radiobutton(right_frame, text="S", value=1, variable=self.red_letter_type)
        red_s.pack()
        red_o = tk.Radiobutton(right_frame, text="O", value=2, variable=self.red_letter_type)
        red_o.pack()
        red_computer = tk.Radiobutton(right_frame, text="Computer", value=2, variable=self.red_player_type)
        red_computer.pack()
        
    def set_board(self, board_frame):
        # frame that holds everything for the game board
        for row in range(self.board_size):
            new_frame = tk.Frame(board_frame)
            new_frame.pack()
            for column in range(self.board_size):
                button = tk.Button(
                    new_frame, text="", font=('Arial', 10, 'bold'),
                    width=4, height=2,
                    command=lambda row=row, column=column: self.controller.handle_board_click(row, column),
                    state=tk.DISABLED
                )
                button.pack(side="left")
                self.game_spaces[row][column] = button
                
    def create_bottom_widgets(self, main_frame):
        # frame that holds everything at the bottom
        bottom_frame = tk.Frame(main_frame, border=1, borderwidth=10, relief="groove")
        bottom_frame.pack(side="bottom", fill="x")

        record_game_check_button = tk.Checkbutton(bottom_frame, text="Record Game")
        record_game_check_button.pack(side="top")

        self.current_turn_label = tk.Label(bottom_frame, text="PRESS 'NEW GAME' TO START", )
        self.current_turn_label.pack(side="top")

        replay_game_button = tk.Button(bottom_frame, text="Replay Game", background="light gray")
        replay_game_button.pack(side="top")

        new_game_button = tk.Button(bottom_frame, text="New Game", background="light gray", command=self.controller.start_new_game)
        new_game_button.pack(side="top")
    
    def create_widgets(self):
        main_frame = tk.Frame(self.root)
        main_frame.pack()
        
        self.create_top_widgets(main_frame)
        
        self.create_left_widgets(main_frame)
        
        self.create_right_widgets(main_frame)
        
        self.board_frame = tk.Frame(main_frame, border=1, borderwidth=10, relief="groove")
        self.board_frame.pack(padx=25, pady=25)
        self.set_board(self.board_frame)
        
        self.create_bottom_widgets(main_frame)

    def update_board_display(self, is_win, game_mode):
        game = self.controller.current_game
        
        if not game:
            return

        game_board = game.game_board
        
        color_data = None
        winner_color = ""
        if game_mode == 1 and is_win:
            color_data = game.get_winning_coords()
            winner_color = game.get_winner().get_color()
        elif game_mode == 2:
            color_data = game.get_color_board()

        for row in range(self.board_size):
            for column in range(self.board_size):
                button = self.game_spaces[row][column]
                symbol = game_board[row][column]
                
                if symbol == " ":
                    if not is_win and not game.check_draw():
                        button.config(text="", state=tk.NORMAL)
                    continue

                button.config(text=symbol, state=tk.DISABLED)
                
                final_color = "black"                 
                if game_mode == 1 and is_win:
                    if (row, column) in color_data:
                        final_color = winner_color
                elif game_mode == 2:
                    sos_color = color_data[row][column]
                    if sos_color:
                        final_color = sos_color
                        
                button.config(disabledforeground=final_color)

    def reset_board(self, board_size):
        self.board_size = board_size
        for widget in self.board_frame.winfo_children():
            widget.destroy()

        self.game_spaces = [[None for _ in range(self.board_size)] for _ in range(self.board_size)]
        
        self.set_board(self.board_frame)
        for row in self.game_spaces:
            for button in row:
                button.config(state=tk.NORMAL, text="")
                
    def disable_board(self):
        for row in self.game_spaces:
            for button in row:
                button.config(state=tk.DISABLED)

    def set_turn_label(self, text):
        self.current_turn_label.config(text=text)
            
    def show_error(self, message):
        messagebox.showerror("ERROR", message)

    # getters
    def get_board_size(self):
        return int(self.board_size_entry.get())

    def get_game_mode(self):
        return self.default_game_mode.get()

    def get_blue_player_type(self):
        return self.blue_player_type.get()

    def get_blue_letter_type(self):
        return self.blue_letter_type.get()
        
    def get_red_player_type(self):
        return self.red_player_type.get()

    def get_red_letter_type(self):
        return self.red_letter_type.get()
