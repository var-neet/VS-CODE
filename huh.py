import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("HACKERS UNDER HAZARD")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Define pixel size for the pixelated effect
pixel_size = 20  # Size of each "pixel" (in terms of screen space)

# Function to create a simple pixel art block
def draw_pixel_art(x, y, color):
    pygame.draw.rect(screen, color, pygame.Rect(x * pixel_size, y * pixel_size, pixel_size, pixel_size))

# Main game loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Quit the game

    # Fill the screen with a black background
    screen.fill(BLACK)

    # Draw a simple pixelated graphic: a 10x10 block pattern
    for y in range(10):
        for x in range(10):
            if (x + y) % 2 == 0:
                draw_pixel_art(x, y, RED)  # Draw red pixels in a checkerboard pattern
            else:
                draw_pixel_art(x, y, GREEN)  # Draw green pixels in a checkerboard pattern

    # Update the display to show changes
    pygame.display.flip()

    # Delay to avoid freezing
    pygame.time.Clock().tick(60)  # Ensures the game runs at 60 FPS

# Quit Pygame
pygame.quit()
sys.exit()
