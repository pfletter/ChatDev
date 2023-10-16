'''
This file contains the Snake class that represents the snake in the game.
'''
import pygame
class Snake:
    def __init__(self):
        self.head = pygame.Rect(400, 300, 20, 20)
        self.body = [self.head]
        self.direction = pygame.K_RIGHT
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.direction != pygame.K_DOWN:
            self.direction = pygame.K_UP
        elif keys[pygame.K_DOWN] and self.direction != pygame.K_UP:
            self.direction = pygame.K_DOWN
        elif keys[pygame.K_LEFT] and self.direction != pygame.K_RIGHT:
            self.direction = pygame.K_LEFT
        elif keys[pygame.K_RIGHT] and self.direction != pygame.K_LEFT:
            self.direction = pygame.K_RIGHT
        if self.direction == pygame.K_UP:
            self.head.y -= 20
        elif self.direction == pygame.K_DOWN:
            self.head.y += 20
        elif self.direction == pygame.K_LEFT:
            self.head.x -= 20
        elif self.direction == pygame.K_RIGHT:
            self.head.x += 20
    def render(self, window):
        for segment in self.body:
            pygame.draw.rect(window, (0, 255, 0), segment)
    def grow(self):
        tail = self.body[-1]
        if self.direction == pygame.K_UP:
            new_segment = pygame.Rect(tail.x, tail.y + 20, 20, 20)
        elif self.direction == pygame.K_DOWN:
            new_segment = pygame.Rect(tail.x, tail.y - 20, 20, 20)
        elif self.direction == pygame.K_LEFT:
            new_segment = pygame.Rect(tail.x + 20, tail.y, 20, 20)
        elif self.direction == pygame.K_RIGHT:
            new_segment = pygame.Rect(tail.x - 20, tail.y, 20, 20)
        self.body.append(new_segment)