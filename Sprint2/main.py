import tkinter as tk
from gui import SOSGUI

if __name__ == "__main__":
    root = tk.Tk()
    root.title("SOS Game")
    window = SOSGUI(root)
    root.mainloop()