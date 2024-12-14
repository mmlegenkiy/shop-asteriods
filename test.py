import pygame
import random

pygame.init()
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake")
green = (0, 255, 0)
red = (255, 0, 60)
font = pygame.font.SysFont("Arial", 20)
clock = pygame.time.Clock()

# Настройки игры
cell_size = 25
snake_speed = 7
snake_length = 1
snake_body = [pygame.Rect(screen_width // 2, screen_height //
                          2, cell_size, cell_size)]
direction = "RIGHT"
next_direction = "RIGHT"

# Функция для создания фруктов


def generate_fruit():
    x = random.randint(0, (screen_width - cell_size) // cell_size) * cell_size
    y = random.randint(0, (screen_height - cell_size) // cell_size) * cell_size
    return pygame.Rect(x, y, cell_size, cell_size)


fruit = generate_fruit()
points = 0
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                next_direction = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                next_direction = "DOWN"
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                next_direction = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                next_direction = "RIGHT"

    direction = next_direction
    head = snake_body[0]
    if direction == "UP":
        new_head = pygame.Rect(
            head.x, head.y - cell_size, cell_size, cell_size)
    elif direction == "DOWN":
        new_head = pygame.Rect(
            head.x, head.y + cell_size, cell_size, cell_size)
    elif direction == "LEFT":
        new_head = pygame.Rect(
            head.x - cell_size, head.y, cell_size, cell_size)
    elif direction == "RIGHT":
        new_head = pygame.Rect(
            head.x + cell_size, head.y, cell_size, cell_size)

    if new_head.x < 0 or new_head.x >= screen_width or new_head.y < 0 or new_head.y >= screen_height:
        game_over = True

    if new_head in snake_body:
        game_over = True

    snake_body.insert(0, new_head)
    if new_head.colliderect(fruit):
        points += 1
        fruit = generate_fruit()
    else:
        snake_body.pop()

    screen.fill((0, 0, 0))
    for part in snake_body:
        pygame.draw.rect(screen, green, part)
    pygame.draw.circle(screen, red, fruit.center, cell_size // 2)

    score_display = font.render(f"Score: {points}", True, (255, 255, 255))
    screen.blit(score_display, (10, 10))
    pygame.display.update()

    clock.tick(snake_speed)

pygame.quit()