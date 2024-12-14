import pygame
import random
import time
from snake_exceptions import SnakeException
from box import Box
from snake import Snake


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
        self.font = pygame.font.SysFont("Arial", 20)
        self.apple = self.generate_box(self.apple_color)
        self.score = 0
        self.score_color = (255, 255, 255)
        snake_head = self.generate_box(self.snake_color)
        self.snake = Snake(snake_head, self.snake_color, random.choice(self.directions))
        # self.clock = pygame.time.Clock()

    def generate_box(self, color):
        x_position = random.randint(2, self.screen_width - 2) * self.cell_size
        y_position = random.randint(2, self.screen_height - 2) * self.cell_size
        box = Box(x_position, y_position, self.cell_size, color)
        return box

    def draw(self):
        self.apple.draw(self.screen)
        self.snake.draw(self.screen)
        score_text = self.font.render(f"Score: {self.score}", True, self.score_color)
        self.screen.blit(score_text, (10, 10))

    def move(self):
        self.snake.move()
        self.screen_intersection_test()

    def screen_intersection_test(self):
        head = self.snake.body[0]
        if head.x_position > self.screen_width * self.cell_size or head.x_position < 0:
            # print(head.x_position)
            raise SnakeException('Screen border intersection')
        if head.y_position > self.screen_height * self.cell_size or head.y_position < 0:
            # print(head.x_position)
            raise SnakeException('Screen border intersection')

    def game_over(self):
        self.screen.fill(self.background_color)
        score_text = self.font.render("Game over", True, self.score_color)
        self.screen.blit(score_text, (self.screen_width * self.cell_size // 2,
                                      self.screen_height * self.cell_size // 2))
        pygame.display.update()
        time.sleep(3)

    def run_game(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.snake.direction != "down":
                        self.snake.change_direction('up')
                    elif event.key == pygame.K_DOWN and self.snake.direction != "up":
                        self.snake.change_direction('down')
                    elif event.key == pygame.K_LEFT and self.snake.direction != "right":
                        self.snake.change_direction('left')
                    elif event.key == pygame.K_RIGHT and self.snake.direction != "left":
                        self.snake.change_direction('right')

            eating = self.snake.body[0].rectangle.colliderect(self.apple.rectangle)
            if eating:
                self.snake.eating()
                self.apple = self.generate_box(self.apple_color)
                self.score += 1

            self.screen.fill(self.background_color)
            try:
                self.move()
            except SnakeException:
                running = False
            self.draw()
            pygame.display.update()
            time.sleep(1)

        self.game_over()
        pygame.quit()
