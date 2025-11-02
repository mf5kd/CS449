import tkinter as tk
from gui import SOSGUI

# This runs the whole program 
# set the root frame for the GUI
if __name__ == "__main__":
    root = tk.Tk()
    root.title("SOS Game")
    window = SOSGUI(root)
    root.mainloop()