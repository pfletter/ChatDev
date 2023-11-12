'''
This is the main file for the Tetris game.
'''
import tkinter as tk
from tetris import TetrisGame
def main():
    root = tk.Tk()
    root.title("Tetris")
    game = TetrisGame(root)
    game.pack()
    root.mainloop()
if __name__ == "__main__":
    main()