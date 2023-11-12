'''
This file contains the Tetromino class which represents the different shapes in the Tetris game.
'''
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