'''
This file contains the TetrisGame class which represents the game logic and GUI.
'''
import tkinter as tk
class TetrisGame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.bind("<Left>", self.move_left)
        self.master.bind("<Right>", self.move_right)
        self.master.bind("<Down>", self.move_down)
        self.score = 0
        self.level = 1
        self.timer = 0
        self.create_widgets()
        self.start_game()
    def create_widgets(self):
        self.score_label = tk.Label(self.master, text="Score: 0")
        self.score_label.pack()
        self.level_label = tk.Label(self.master, text="Level: 1")
        self.level_label.pack()
        self.timer_label = tk.Label(self.master, text="Timer: 0")
        self.timer_label.pack()
        self.canvas = tk.Canvas(self.master, width=200, height=400, bg="white")
        self.canvas.pack()
    def start_game(self):
        self.timer = 0
        self.score = 0
        self.level = 1
        self.update_score()
        self.update_level()
        self.update_timer()
        self.draw_board()
        self.draw_block()
        self.master.after(8000, self.move_block_down)
    def update_score(self):
        self.score_label.config(text=f"Score: {self.score}")
    def update_level(self):
        self.level_label.config(text=f"Level: {self.level}")
    def update_timer(self):
        self.timer_label.config(text=f"Timer: {self.timer}")
        self.timer += 1
        self.master.after(1000, self.update_timer)
    def draw_board(self):
        self.canvas.delete("all")
        self.canvas.create_rectangle(0, 0, 200, 400, outline="black")
    def draw_block(self):
        self.current_block = self.canvas.create_rectangle(90, 0, 110, 20, fill="red")
    def move_block_down(self):
        if not self.check_collision():
            self.canvas.move(self.current_block, 0, 20)
            self.master.after(800, self.move_block_down)
        else:
            self.clear_rows()
            self.draw_block()
    def move_left(self, event):
        if not self.check_collision():
            self.canvas.move(self.current_block, -20, 0)
    def move_right(self, event):
        if not self.check_collision():
            self.canvas.move(self.current_block, 20, 0)
    def move_down(self, event):
        if not self.check_collision():
            self.canvas.move(self.current_block, 0, 20)
    def check_collision(self):
        coords = self.canvas.coords(self.current_block)
        if coords[3] >= 400:
            return True
        return False
    def clear_rows(self):
        rows_to_clear = []
        for row in range(0, 400, 20):
            if self.check_row_complete(row):
                rows_to_clear.append(row)
        for row in rows_to_clear:
            self.canvas.delete(tk.ALL)
            self.canvas.move(tk.ALL, 0, 20)
        self.score += len(rows_to_clear) * 100
        self.update_score()
    def check_row_complete(self, row):
        for col in range(0, 200, 20):
            if not self.canvas.find_overlapping(col, row, col + 20, row + 20):
                return False
        return True