import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 600
APPLE_RADIUS = 20
HAND_SIZE = 50

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Create the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Apple")

# Initial positions
apple_x = WIDTH // 2
apple_y = 0
hand_x = (WIDTH - HAND_SIZE) // 2
hand_y = HEIGHT - HAND_SIZE

# Initialize variables
apple_falling = True
score = 0

# Font for displaying score
font = pygame.font.Font(None, 36)

# Game loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Create Rect objects for the apple and the hand
            apple_rect = pygame.Rect(apple_x - APPLE_RADIUS, apple_y - APPLE_RADIUS, 2 * APPLE_RADIUS, 2 * APPLE_RADIUS)
            hand_rect = pygame.Rect(hand_x, hand_y, HAND_SIZE, HAND_SIZE)

            # Check if the apple and the hand Rect objects collide
            if apple_rect.colliderect(hand_rect):
                score += 1
                apple_falling = False
                apple_x = WIDTH // 2
                apple_y = 0
                apple_falling = True

    if apple_falling:
        apple_y += 5  # Adjust the falling speed

    # Clear the screen
    screen.fill(WHITE)

    # Draw the apple
    pygame.draw.circle(screen, RED, (apple_x, apple_y), APPLE_RADIUS)

    # Get the mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Update the hand position based on the mouse
    hand_x = mouse_x - HAND_SIZE // 2
    hand_y = mouse_y - HAND_SIZE // 2

    # Draw the hand
    pygame.draw.rect(screen, RED, (hand_x, hand_y, HAND_SIZE, HAND_SIZE))

    # Display the score
    score_text = font.render("Score: " + str(score), True, RED)
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Check if the apple is out of the screen
    if apple_y > HEIGHT:
        apple_falling = False
        apple_x = WIDTH // 2
        apple_y = 0
        pygame.time.delay(1000)  # Delay before dropping the next apple
        apple_falling = True

    clock.tick(60)
