import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Mirror Battle - Reach the Checkpoint')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Player settings
player_width, player_height = 50, 50
player_speed = 5

# Initialize player and mirror (enemy)
player = pygame.Rect(WIDTH//4, HEIGHT//2, player_width, player_height)
mirror = pygame.Rect(WIDTH//2, HEIGHT//2, player_width, player_height)

# Checkpoint settings
checkpoint = pygame.Rect(WIDTH - 100, HEIGHT - 100, 50, 50)  # Checkpoint in the bottom right corner

# Game loop
clock = pygame.time.Clock()
running = True
game_won = False
game_lost = False

while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_won and not game_lost:
        # Get keys pressed (player control)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            player.x -= player_speed
        if keys[pygame.K_RIGHT]:
            player.x += player_speed
        if keys[pygame.K_UP]:
            player.y -= player_speed
        if keys[pygame.K_DOWN]:
            player.y += player_speed

        # The mirror enemy mimics the player's movement (but with a slight delay or speed)
        if player.x < mirror.x:
            mirror.x -= 1
        elif player.x > mirror.x:
            mirror.x += 1
        if player.y < mirror.y:
            mirror.y -= 1
        elif player.y > mirror.y:
            mirror.y += 1

        # Check for win or lose condition (who reaches the checkpoint first)
        if player.colliderect(checkpoint):
            game_won = True
        if mirror.colliderect(checkpoint):
            game_lost = True

    # Draw player, mirror, and checkpoint
    pygame.draw.rect(screen, BLACK, player)
    pygame.draw.rect(screen, RED, mirror)
    pygame.draw.rect(screen, GREEN, checkpoint)  # Draw the checkpoint

    # Display win or lose message
    if game_won:
        font = pygame.font.SysFont(None, 55)
        win_text = font.render("You Win!", True, (0, 128, 0))
        screen.blit(win_text, (WIDTH//2 - win_text.get_width()//2, HEIGHT//4))

    if game_lost:
        font = pygame.font.SysFont(None, 55)
        lose_text = font.render("You Lose!", True, (255, 0, 0))
        screen.blit(lose_text, (WIDTH//2 - lose_text.get_width()//2, HEIGHT//4))

    # Update screen
    pygame.display.update()

    # Set frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
