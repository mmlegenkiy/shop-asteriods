import pygame
import time
import random

from pygame.transform import scale
from space_ship import  Spaceship
from asteroid import Asteroid


class Game:
    """
    Головний клас для керування грою
    """
    def __init__(self):
        """
        Ініціалізується pygame, створюються головні константи гри, завантажується фонове зобарження та звуки.
        """
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Asteroids")
        self.background = pygame.image.load("images/background.jpg")
        self.background = scale(self.background, (self.screen_width, self.screen_height))
        self.ship = Spaceship(400, 400)
        self.asteroids = []
        self.gap = 100
        pygame.font.init()
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        self.game_over_font = pygame.font.SysFont('Comic Sans MS', 100)
        self.timer = pygame.time.Clock()
        self.running = True

        pygame.mixer.music.load("sounds/background_sound.mp3")
        pygame.mixer.music.play()
        self.explosion_sound = pygame.mixer.Sound("sounds/explosion_sound1.mp3")

    def display(self):
        """
        Метод для відображення змін в грі. Малюється фонове зображення, космічий корабель (за наявності перетину
        з астероїдом при цьому буде малюватись і вибух), астеорїди; відображається кількість життів
         (здоров'я) космічного корабля.
        :return:
        """
        self.screen.blit(self.background, (0, 0))
        self.ship.draw(self.screen)
        for asteroid in self.asteroids:
            asteroid.move(self.screen_height)
            asteroid.draw(self.screen)
        text = self.font.render(f'Health: {self.ship.life}', False, (255, 255, 255))
        self.screen.blit(text, (20, 20))

    @staticmethod
    def probability(p):
        """
        Статичний метод, який із вірогідністю p видає True, інакше - Fale
        :param p: вірогідність, число з плаваючою крапкою
        :return: логічна змінна
        """
        return True if random.randint(1, 1000) < 1000 * p else False

    def generate_asteroid(self):
        """Метод для створення астероїда у випадковому місці зверху екрана.
        Астероїд генерується поза екраном, на відстані self.gap від верху, а потім рухається вниз"""
        asteroid_x = random.randint(-self.gap, self.screen_width + self.gap)
        asteroid_y = -self.gap
        asteroid = Asteroid(asteroid_x, asteroid_y)
        self.asteroids.append(asteroid)

    def game_over(self):
        """
        Метод для закінчення гри. Малює надпис "Game over" на чорному тлі
        і через 3 секунди завершує гру (перемикає змінну self.running у False)
        """
        self.screen.fill("black")
        text = self.game_over_font.render(f'Game over', False, "white")
        self.screen.blit(text, (self.screen_width // 2 - text.get_width() // 2,
                                self.screen_height // 2 - text.get_height() // 2))
        pygame.display.update()
        time.sleep(3)
        self.running = False

    def run(self):
        """
        Головний цикл гри. Тут: з ймовірністю 0.1 генерується астероїд, оброблюється
        натискання клавіш ліворуч та праворуч для руху космічного корабля, здійснюється
        рух корабля, у разі перетину корабля із астероїдом виводиться звук вибуху,
        онолвюється відображення у віконці гри (викликається метод display), якщо у корабля
        закінчуються життя, то гра завершується (викликається метод game_over).
        """
        left = False # рух корабля ліворуч
        right = False # рух корабля праворуч
        while self.running:
            self.timer.tick(30)
            if Game.probability(0.1):
                self.generate_asteroid()
            # обробка натискань клавіш
            for e in pygame.event.get():
                if e.type == pygame.KEYDOWN and e.key == pygame.K_LEFT:
                    left = True
                if e.type == pygame.KEYDOWN and e.key == pygame.K_RIGHT:
                    right = True
                if e.type == pygame.KEYUP and e.key == pygame.K_LEFT:
                    left = False
                if e.type == pygame.KEYUP and e.key == pygame.K_RIGHT:
                    right = False
                if e.type == pygame.QUIT:
                    raise SystemExit("QUIT")
            self.ship.change_velocity(left, right) # зміна швидкості корабля
            self.ship.move(self.screen_width) # рух корабля
            if self.ship.check_collisions(self.asteroids):
                self.explosion_sound.play() #у випадку зіткнення з астероїдом виводимо звук вибуху
            self.display() # змінюємо відображення
            if self.ship.life < 1:
                self.game_over() # вихід із гри
            pygame.display.update()
