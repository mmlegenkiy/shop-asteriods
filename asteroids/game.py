# from os import environ
# environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame
import time
import random

from pygame.transform import scale
from space_ship import  Spaceship
from asteroid import Asteroid


class Game:
    def __init__(self):
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Asteroids")
        self.background = pygame.image.load("images/background.jpg")
        self.background = scale(self.background, (self.screen_width, self.screen_height))
        self.ship = Spaceship(400, 400)
        self.asteroids = []
        pygame.font.init()
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        self.timer = pygame.time.Clock()
        # self.background_sound = pygame.mixer.Sound("sounds/background_sound.mp3")
        # self.explosion_sound = pygame.mixer.Sound("sounds/explosion_sound1.mp3")

    def display(self):
        self.screen.blit(self.background, (0, 0))
        self.ship.draw(self.screen)
        for asteroid in self.asteroids:
            asteroid.update((self.screen_width, self.screen_height))
            asteroid.draw(self.screen)
        text = self.font.render(f'Health: {self.ship.life}', False, (255, 255, 255))
        self.screen.blit(text, (20, 20))

    def run(self):
        left = False
        right = False
        while True:
            #     self.explosion_sound.play(0)
            value = random.randint(1, 1000)
            if value > 900:
                asteroid_x = random.randint(-100, 700)
                asteroid_y = -100
                asteroid = Asteroid(asteroid_x, asteroid_y)
                self.asteroids.append(asteroid)

            self.timer.tick(30)

            # for asteroid in self.asteroids:
            #     if self.ship.rect.colliderect(asteroid.rect):
            #         self.ship.life -= 1
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

            self.ship.update(left, right, self.asteroids)
            self.display()
            pygame.display.update()
            # time.sleep(0.1)
