'''
This file contains the Tetris class which represents the game logic and handles user input.
'''
import pygame
import sys
import random
from tetromino import Tetromino
class Tetris:
    def __init__(self):
        self.width = 10
        self.height = 20
        self.grid = [[0] * self.width for _ in range(self.height)]
        self.current_piece = None
        self.next_piece = None
        self.score = 0
        self.level = 1
        self.lines_cleared = 0
    def run(self):
        # Initialize the game window
        pygame.init()
        self.screen = pygame.display.set_mode((self.width * 30, self.height * 30))
        pygame.display.set_caption("Tetris")
        # Game loop
        while True:
            self.handle_events()
            self.update()
            self.render()
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.move_left()
                elif event.key == pygame.K_RIGHT:
                    self.move_right()
                elif event.key == pygame.K_DOWN:
                    self.move_down()
                elif event.key == pygame.K_UP:
                    self.rotate()
    def update(self):
        if self.current_piece is None:
            self.spawn_piece()
        else:
            if not self.move_down():
                self.lock_piece()
                self.clear_lines()
                self.spawn_piece()
    def render(self):
        self.screen.fill((0, 0, 0))
        self.draw_grid()
        pygame.display.flip()
    def draw_grid(self):
        cell_size = 30
        colors = [(0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255), (255, 255, 255)]
        for row in range(self.height):
            for col in range(self.width):
                if self.grid[row][col] != 0:
                    x = col * cell_size
                    y = row * cell_size
                    pygame.draw.rect(self.screen, colors[self.grid[row][col]], (x, y, cell_size, cell_size))
    def move_left(self):
        if self.current_piece is not None:
            if self.is_valid_move(self.current_piece, self.current_piece.x - 1, self.current_piece.y):
                self.current_piece.move_left()
    def move_right(self):
        if self.current_piece is not None:
            if self.is_valid_move(self.current_piece, self.current_piece.x + 1, self.current_piece.y):
                self.current_piece.move_right()
    def move_down(self):
        if self.current_piece is not None:
            if self.is_valid_move(self.current_piece, self.current_piece.x, self.current_piece.y + 1):
                self.current_piece.move_down()
                return True
            else:
                return False
    def rotate(self):
        if self.current_piece is not None:
            rotated_piece = self.current_piece.rotate()
            if self.is_valid_move(rotated_piece, rotated_piece.x, rotated_piece.y):
                self.current_piece = rotated_piece
    def spawn_piece(self):
        piece_type = random.choice(['I', 'J', 'L', 'O', 'S', 'T', 'Z'])
        self.current_piece = Tetromino(piece_type, self.width // 2, 0)
    def is_valid_move(self, piece, new_x, new_y):
        shape = piece.get_shape()
        for row in range(len(shape)):
            for col in range(len(shape[row])):
                if shape[row][col] != 0:
                    if (
                        new_x + col < 0
                        or new_x + col >= self.width
                        or new_y + row >= self.height
                        or self.grid[new_y + row][new_x + col] != 0
                    ):
                        return False
        return True
    def lock_piece(self):
        shape = self.current_piece.get_shape()
        for row in range(len(shape)):
            for col in range(len(shape[row])):
                if shape[row][col] != 0:
                    self.grid[self.current_piece.y + row][self.current_piece.x + col] = shape[row][col]
    def clear_lines(self):
        lines_cleared = 0
        for row in range(self.height):
            if all(cell != 0 for cell in self.grid[row]):
                self.grid.pop(row)
                self.grid.insert(0, [0] * self.width)
                lines_cleared += 1
        self.lines_cleared += lines_cleared
        self.score += lines_cleared * 100
class Tetromino:
    def __init__(self, piece_type, x, y):
        self.piece_type = piece_type
        self.x = x
        self.y = y
    def move_left(self):
        self.x -= 1
    def move_right(self):
        self.x += 1
    def move_down(self):
        self.y += 1
    def rotate(self):
        if self.piece_type == 'I':
            return Tetromino('I', self.x, self.y)
        elif self.piece_type == 'J':
            return Tetromino('J', self.x, self.y)
        elif self.piece_type == 'L':
            return Tetromino('L', self.x, self.y)
        elif self.piece_type == 'O':
            return Tetromino('O', self.x, self.y)
        elif self.piece_type == 'S':
            return Tetromino('S', self.x, self.y)
        elif self.piece_type == 'T':
            return Tetromino('T', self.x, self.y)
        elif self.piece_type == 'Z':
            return Tetromino('Z', self.x, self.y)
    def get_shape(self):
        if self.piece_type == 'I':
            return [
                [1, 1, 1, 1]
            ]
        elif self.piece_type == 'J':
            return [
                [1, 0, 0],
                [1, 1, 1]
            ]
        elif self.piece_type == 'L':
            return [
                [0, 0, 1],
                [1, 1, 1]
            ]
        elif self.piece_type == 'O':
            return [
                [1, 1],
                [1, 1]
            ]
        elif self.piece_type == 'S':
            return [
                [0, 1, 1],
                [1, 1, 0]
            ]
        elif self.piece_type == 'T':
            return [
                [0, 1, 0],
                [1, 1, 1]
            ]
        elif self.piece_type == 'Z':
            return [
                [1, 1, 0],
                [0, 1, 1]
            ]