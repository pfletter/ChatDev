'''
This file contains the Food class that represents the food in the game.
'''
import pygame
import random
class Food:
    def __init__(self):
        self.rect = pygame.Rect(0, 0, 20, 20)
        self.generate()
    def generate(self):
        x = random.randint(0, 39) * 20
        y = random.randint(0, 29) * 20
        self.rect.topleft = (x, y)
    def render(self, window):
        pygame.draw.rect(window, (255, 0, 0), self.rect)