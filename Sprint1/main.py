import tkinter as tk
from gui import SOSGUI

if __name__ == "__main__":
    root = tk.Tk()
    window = SOSGUI(root, 9)
    root.mainloop()