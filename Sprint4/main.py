import tkinter as tk
from gui import SOSGUI
from controller import GameController
# This runs the whole program 
# set the root frame for the GUI
if __name__ == "__main__":
    root = tk.Tk()
    root.title("SOS Game")
    controller = GameController()
    window = SOSGUI(root, controller)
    controller.set_view(window)
    root.mainloop()
