# Напишіть лайт-версію гри "Змійка", використовуючи Pygame. Змійка їсть червоні яблука,
# які з'являються у випадкових позиціях у межах ігрового поля, та додає у довжині після
# кожного яблука. При зіткненні з хвостом чи межею вікна гра закінчується.

import pygame
import random

class Box:
    def __init__(self, x_position, y_position, size, color, direction, speed):
        self.x_position = x_position
        self.y_position = y_position
        self.size = size
        self.color = color
        self.direction = direction
        self.speed = speed
        self.rectangle = pygame.Rect(self.x_position, self.y_position, self.size, self.size)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rectangle)

    def move(self):
        if self.direction == 'left':
            self.x_position -= self.speed
        elif self.direction == 'right':
            self.x_position += self.speed
        elif self.direction == 'up':
            self.y_position -= self.speed
        elif self.direction == 'down':
            self.y_position += self.speed
        self.rectangle = pygame.Rect(self.x_position, self.y_position, self.size, self.size)


class Snake:
    def __init__(self, box, color):
        box.color = color
        self.body = [box]
        self.color = color

    def collide_box_test(self, box):
        head = self.body[0]
        if head.direction == 'up':
            pass
        elif head.direction == 'down':
            pass

    def eat_apple(self):
        head = self.body[0]
        new_head = head
        new_head.move()
        # apple.color = self.color
        # apple.direction = self.body[0].direction
        # apple.speed = self.body[0].speed
        self.body.insert(0, new_head)

    def draw(self, screen):
        for box in self.body:
            box.draw(screen)

    def move(self):
        for box in self.body:
            box.move()

    def change_direction(self, direction):
        self.body[0].direction = direction


class Game:
    directions = ['left', 'right', 'up', 'down']
    def __init__(self):
        pygame.init()
        self.cell_size = 20
        self.screen_width = 30
        self.screen_height = 30
        self.screen = pygame.display.set_mode((self.screen_width * self.cell_size, self.screen_height * self.cell_size))
        pygame.display.set_caption("Snake")
        self.font = pygame.font.SysFont("Consolas", 20)
        self.background_color = (0, 0, 0)
        self.snake_color = (0, 255, 0)
        self.apple_color = (255, 0, 0)
        self.snake_speed = 5
        self.apple = self.generate_box(self.apple_color, None, 0)
        snake_head = self.generate_box(self.snake_color, random.choice(self.directions), self.snake_speed)
        self.snake = Snake(snake_head, self.snake_color)
        self.clock = pygame.time.Clock()

    def generate_box(self, color, direction, speed):
        x_position = random.randint(2, self.screen_width - 2) * self.cell_size
        y_position = random.randint(2, self.screen_height - 2) * self.cell_size
        box = Box(x_position, y_position, self.cell_size, color, direction, speed)
        return box

    def draw(self):
        self.apple.draw(self.screen)
        self.snake.draw(self.screen)

    def move(self):
        self.snake.move()

    def run_game(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.snake.body[0].direction != "down":
                        self.snake.change_direction('up')
                    elif event.key == pygame.K_DOWN and self.snake.body[0].direction != "up":
                        self.snake.change_direction('down')
                    elif event.key == pygame.K_LEFT and self.snake.body[0].direction != "right":
                        self.snake.change_direction('left')
                    elif event.key == pygame.K_RIGHT and self.snake.body[0].direction != "left":
                        self.snake.change_direction('right')

            eating = self.snake.body[0].rectangle.colliderect(self.apple.rectangle)
            if eating:
                self.snake.eat_apple()
                self.apple = self.generate_box(self.apple_color, None, 0)

            self.screen.fill(self.background_color)
            self.move()
            self.draw()
            pygame.display.update()
            self.clock.tick(self.snake_speed)

        pygame.quit()


if __name__ == "__main__":
    app = Game()
    app.run_game()


# pygame.init()
# screen_width = 600
# screen_height = 600
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption("Snake")
# green = (0, 255, 0)
# red = (255, 0, 0)
# font = pygame.font.SysFont("Arial", 20)
# clock = pygame.time.Clock()
#
# class Box:
#
#
# # Основні параметри гри
# cell_size = 10
# snake_speed = 5
# # snake_length = ?
# # snake_body = []
#
# # Створюємо змію та визначаємо напрям її руху
# # for i in range(snake_length):
# #     snake_body.append(pygame.Rect(pos_x, pos_y, cell_size, cell_size))
# # snake_direction = ?
# # new_direction = ?
# # Визначаємо випадкове положення для яблука
# # apple_position = pygame.Rect(random_x, random_y, cell_size, cell_size)
#
# game_over = False
# while not game_over:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             game_over = True
#         # Визначаємо новий напрямок руху змії
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_UP: # and snake_direction != "down":
#                 pass
#             elif event.key == pygame.K_DOWN: # and snake_direction != "up":
#                 pass
#             elif event.key == pygame.K_LEFT: # and snake_direction != "right":
#                 pass
#             elif event.key == pygame.K_RIGHT: # and snake_direction != "left":
#                 pass
#
#     # Керування змією
#
#     # Перевіряємо, чи з'їла змія яблуко
#     # if snake_body[0].colliderect(apple_position):
#         # Створюємо нове яблуко у випадковому місці
#         # Збільшуємо змію
#
#     # Перевірка на зіткнення зі стінками
#     # if ?:
#     #     game_over = True
#
#     # Перевірка на зіткнення голови змії із власним тілом
#
#     screen.fill((0, 0, 0))
#     # Малюємо змію
#
#     # Малюємо яблуко
#     # pygame.draw.circle(screen, color, apple_position.center, cell_size / 2)
#
#     # Друкуємо кількість з'їдених яблук
#     # score_text = font.render(string, True, (255, 255, 255))
#     # screen.blit(score_text, (10, 10))
#     # pygame.display.update()
#
#     clock.tick(snake_speed)
#
# pygame.quit()