'''
This is the main file that runs the snake game.
'''
import pygame
from game import Game
def main():
    # Initialize pygame
    pygame.init()
    # Set up the game window
    window_width = 800
    window_height = 600
    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Snake Game")
    # Create a new game instance
    game = Game(window)
    # Game loop
    running = True
    while running:
        # Process events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # Update game state
        game.update()
        # Render game
        game.render()
        # Update display
        pygame.display.flip()
    # Quit pygame
    pygame.quit()
if __name__ == "__main__":
    main()