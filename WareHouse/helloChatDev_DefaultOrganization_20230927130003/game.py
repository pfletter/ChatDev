'''
This file contains the Game class that manages the snake game.
'''
from snake import Snake
from food import Food
class Game:
    def __init__(self, window):
        self.window = window
        self.snake = Snake()
        self.food = Food()
    def update(self):
        self.snake.update()
        self.check_collision()
    def render(self):
        self.window.fill((0, 0, 0))
        self.snake.render(self.window)
        self.food.render(self.window)
    def check_collision(self):
        if self.snake.head.colliderect(self.food.rect):
            self.snake.grow()
            self.food.generate()