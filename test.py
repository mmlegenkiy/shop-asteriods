# Напишіть лайт-версію гри "Змійка", використовуючи Pygame. Змійка їсть червоні яблука,
# які з'являються у випадкових позиціях у межах ігрового поля, та додає у довжині після
# кожного яблука. При зіткненні з хвостом чи межею вікна гра закінчується.

import pygame
import random

pygame.init()
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake")
green = (0, 255, 0)
red = (255, 0, 0)
font = pygame.font.SysFont("Arial", 20)
clock = pygame.time.Clock()

# Основні параметри гри
cell_size = 20
snake_speed = 5
snake_length = 1
snake_body = [pygame.Rect(screen_width // 2, screen_height // 2, cell_size, cell_size)]
snake_direction = "RIGHT"
new_direction = "RIGHT"

# Визначаємо випадкове положення для яблука
def random_apple_position():
    x = random.randint(0, (screen_width - cell_size) // cell_size) * cell_size
    y = random.randint(0, (screen_height - cell_size) // cell_size) * cell_size
    return pygame.Rect(x, y, cell_size, cell_size)

apple_position = random_apple_position()
score = 0
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != "DOWN":
                new_direction = "UP"
            elif event.key == pygame.K_DOWN and snake_direction != "UP":
                new_direction = "DOWN"
            elif event.key == pygame.K_LEFT and snake_direction != "RIGHT":
                new_direction = "LEFT"
            elif event.key == pygame.K_RIGHT and snake_direction != "LEFT":
                new_direction = "RIGHT"

    # Оновлюємо напрямок руху змії
    snake_direction = new_direction
    head = snake_body[0]
    if snake_direction == "UP":
        new_head = pygame.Rect(head.x, head.y - cell_size, cell_size, cell_size)
    elif snake_direction == "DOWN":
        new_head = pygame.Rect(head.x, head.y + cell_size, cell_size, cell_size)
    elif snake_direction == "LEFT":
        new_head = pygame.Rect(head.x - cell_size, head.y, cell_size, cell_size)
    elif snake_direction == "RIGHT":
        new_head = pygame.Rect(head.x + cell_size, head.y, cell_size, cell_size)

    # Перевіряємо зіткнення зі стінками
    if new_head.x < 0 or new_head.x >= screen_width or new_head.y < 0 or new_head.y >= screen_height:
        game_over = True

    # Перевірка на зіткнення голови змії із власним тілом
    if new_head in snake_body:
        game_over = True

    # Додаємо нову голову
    snake_body.insert(0, new_head)

    # Перевіряємо, чи з'їла змія яблуко
    if new_head.colliderect(apple_position):
        score += 1
        apple_position = random_apple_position()
    else:
        snake_body.pop()  # Видаляємо хвіст, якщо яблуко не з'їдене

    # Очищаємо екран
    screen.fill((0, 0, 0))

    # Малюємо змію
    for segment in snake_body:
        pygame.draw.rect(screen, green, segment)

    # Малюємо яблуко
    pygame.draw.circle(screen, red, apple_position.center, cell_size / 2)

    # Друкуємо кількість з'їдених яблук
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    pygame.display.update()

    clock.tick(snake_speed)

pygame.quit()