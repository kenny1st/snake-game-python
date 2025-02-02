
---

### **Basic Code for `main.py`**  
```python
import pygame
import random

# Initialize Pygame
pygame.init()

# Game Settings
WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Create Game Window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Snake & Food Initialization
snake = [(100, 100), (80, 100), (60, 100)]
food = (random.randint(0, WIDTH // GRID_SIZE - 1) * GRID_SIZE,
        random.randint(0, HEIGHT // GRID_SIZE - 1) * GRID_SIZE)
direction = (GRID_SIZE, 0)

# Game Loop
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(BLACK)
    
    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, GRID_SIZE):
                direction = (0, -GRID_SIZE)
            elif event.key == pygame.K_DOWN and direction != (0, -GRID_SIZE):
                direction = (0, GRID_SIZE)
            elif event.key == pygame.K_LEFT and direction != (GRID_SIZE, 0):
                direction = (-GRID_SIZE, 0)
            elif event.key == pygame.K_RIGHT and direction != (-GRID_SIZE, 0):
                direction = (GRID_SIZE, 0)

    # Move Snake
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    if new_head in snake or new_head[0] < 0 or new_head[1] < 0 or new_head[0] >= WIDTH or new_head[1] >= HEIGHT:
        running = False  # Game Over
    else:
        snake.insert(0, new_head)
        if new_head == food:
            food = (random.randint(0, WIDTH // GRID_SIZE - 1) * GRID_SIZE,
                    random.randint(0, HEIGHT // GRID_SIZE - 1) * GRID_SIZE)
        else:
            snake.pop()

    # Draw Food
    pygame.draw.rect(screen, RED, (*food, GRID_SIZE, GRID_SIZE))

    # Draw Snake
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, GRID_SIZE, GRID_SIZE))

    pygame.display.flip()
    clock.tick(10)  # Adjust speed

pygame.quit()
