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
        textsurface = self.font.render(f'HP: {self.ship.life}', False, (255, 255, 255))
        self.screen.blit(textsurface, (20, 20))
        # life = self.font.render(f'HP: {self.ship.life}', False, (255, 255, 255))
        # self.screen.blit(life, (20, 20))

    def run(self):



        left = False
        right = False
        explosion_sound = False
        while True:
            # if explosion_sound:
            #     # pygame.mixer.pause()
            #     # pygame.mixer.unpause()
            #     self.explosion_sound.play(0)
            # # else:
            # #     self.background_sound.play(-1)
            # # с некоторой вероятность будем добавлять астероиды сверху экрана
            value = random.randint(1, 1000)
            # print(value)
            if value > 900:
                # выбираем координату по оси x
                asteroid_x = random.randint(-100, 700)
                # выбираем точку за верхней граничей экрана
                asteroid_y = -100
                # создаем астероид
                asteroid = Asteroid(asteroid_x, asteroid_y)
                # print('I am here')
                # и добавляем его в группу
                self.asteroids.append(asteroid)

            self.timer.tick(60)

            # для каждого астероида
            for asteroid in self.asteroids:
                # если область, занимаемая астероидом пересекает область корабля
                if self.ship.rect.colliderect(asteroid.rect):
                    # уменьшаем жизнь
                    self.ship.life -= 1


            for e in pygame.event.get():
                if e.type == pygame.KEYDOWN and e.key == pygame.K_LEFT:
                    # print('left')
                    left = True
                if e.type == pygame.KEYDOWN and e.key == pygame.K_RIGHT:
                    # print('right')
                    right = True
                if e.type == pygame.KEYUP and e.key == pygame.K_LEFT:
                    left = False
                if e.type == pygame.KEYUP and e.key == pygame.K_RIGHT:
                    right = False
                if e.type == pygame.QUIT:
                    raise SystemExit("QUIT")

            explosion_sound = self.ship.update(left, right, self.asteroids)
            print(explosion_sound)
            self.display()
            # print(len(self.asteroids))
            for asteroid in self.asteroids:
                asteroid.update()
                asteroid.draw(self.screen)
            pygame.display.update()
            time.sleep(0.1)