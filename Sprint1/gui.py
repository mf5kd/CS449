import tkinter as tk
from human import Human

class SOSGUI:
    def __init__(self, root, board_size):
        self.root = root
        self.root.title("SOS Game")
        self.root.resizable(False, False)
        self.board_size = board_size
        self.game = None
        self.game_spaces = [[None for x in range(board_size)] for x in range(board_size)]
        
        self.player = tk.StringVar(value="Human")
        
        self.create_widgets()
    
    def create_widgets(self):
        main_frame = tk.Frame(self.root)
        main_frame.pack()
        
        # frame that holds the check buttons to choose between Simple game or General Game and there labels
        top_frame = tk.Frame(main_frame, border=1, borderwidth=10, relief="groove")# {-> # child of root frame
        top_frame.pack(side="top", fill="x")
        
        game_type_label = tk.Label(top_frame, text="SOS", border=1, relief="solid", font=("TkDefaultFont", 20) )
        game_type_label.pack(side="left")

        simple_game_radio_button = tk.Radiobutton(top_frame, text="Simple Game", value=1, variable="game mode")
        simple_game_radio_button.pack(side="left")

        general_game_radio_button = tk.Radiobutton(top_frame, text="General Game", value=2, variable="game mode")
        general_game_radio_button.pack(side="left")
        
        # frame that hold the label and the entry for the board Size
        board_size_frame = tk.Frame(top_frame)# {-> # is a child of the top frame
        board_size_frame.pack(side="right", fill="x")

        board_size_label = tk.Label(board_size_frame, text="Board Size")
        board_size_label.pack(side="left")

        Board_size_entry = tk.Entry(board_size_frame, width=2, border=5, relief="solid", font=("TkDefaultFont", 15))
        Board_size_entry.pack(side="left")# <-} #
        # <-} #
        
        
        # frame that hold things to the left
        # holds that check Radio button for where blue is a human or computer
        # what letter they are placing
        left_frame = tk.Frame(main_frame, border=1, borderwidth=10, relief="groove")# {-> # is a child of the root frame
        left_frame.pack(side="left", fill="y")

        blue_player_label = tk.Label(left_frame, text="Blue Player")
        blue_player_label.pack()

        blue_human = tk.Radiobutton(left_frame, text="Human", value=1, variable="blue player type")
        blue_human.pack()
        blue_o = tk.Radiobutton(left_frame, text="O", value=1, variable="blue letter type")
        blue_o.pack()
        blue_s = tk.Radiobutton(left_frame, text="S", value=2, variable="blue letter type")
        blue_s.pack()
        blue_computer = tk.Radiobutton(left_frame, text="Computer", value=2, variable="blue player type")
        blue_computer.pack()# <-} #
        
        
        # frame that hold things to the right
        # holds that check buttons for where red is a human or computer
        # what letter they are placing
        right_frame = tk.Frame(main_frame, border=1, borderwidth=10, relief="groove")# {-> # is a child of the root frame
        right_frame.pack(side="right", fill="y")

        red_player_label = tk.Label(right_frame, text="Red Player")
        red_player_label.pack()

        red_human = tk.Radiobutton(right_frame, text="Human", value=1, variable="red player type")
        red_human.pack()
        red_o = tk.Radiobutton(right_frame, text="O", value=1, variable="red letter type")
        red_o.pack()
        red_s = tk.Radiobutton(right_frame, text="S", value=2, variable="red letter type")
        red_s.pack()
        red_computer = tk.Radiobutton(right_frame, text="Computer", value=2, variable="red player type")
        red_computer.pack()# <-} #
        
        # frame that holds everything for the game board
        board_frame = tk.Frame(main_frame, border=1, borderwidth=10, relief="groove")
        board_frame.pack()

        for row in range(self.board_size):
            new_frame = tk.Frame(board_frame)
            new_frame.pack()
            for column in range(self.board_size):
                button = tk.Button(
                    new_frame, text="", font=('Arial', 10, 'bold'),
                    width=4, height=2,
                    command=lambda row=row, column=column: self.blank_board_space_click(row, column)
                ).pack(side="left")
                self.game_spaces[row][column] = button
                
        

        # frame that holds everything at the bottom
        bottom_frame = tk.Frame(main_frame, border=1, borderwidth=10, relief="groove")# {-> # child of root frame
        bottom_frame.pack(side="bottom", fill="x")

        record_game_check_button = tk.Checkbutton(bottom_frame, text="Record Game")
        record_game_check_button.pack(side="top")

        current_turn_label = tk.Label(bottom_frame, text="Current Turn blue or red", )
        current_turn_label.pack(side="top")

        replay_game_radio_button = tk.Button(bottom_frame, text="Replay Game", background="light gray")
        replay_game_radio_button.pack(side="top")

        new_game_radio_button = tk.Button(bottom_frame, text="New Game", background="light gray")
        new_game_radio_button.pack(side="top")
        # <-} #
        
    def blank_board_space_click(self, row, column):
        pass