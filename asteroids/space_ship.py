import pygame
import random
from pygame.transform import scale
from explosion import Explosion


class Spaceship(pygame.sprite.Sprite):
    def __init__(self, x_position, y_position):
        pygame.sprite.Sprite.__init__(self)
        self.width = 50
        self.height = 100
        self.rect = pygame.Rect(x_position, y_position, self.width, self.height)
        self.image = scale(pygame.image.load("images/ship.png"), (self.width, self.height))
        self.x_velocity = 0
        self.y_velocity = 0
        self.life = 100
        self.explosions = []

    def draw(self, screen):
        # print(self.rect.x)
        screen.blit(self.image, (self.rect.x, self.rect.y))
        for explosion in self.explosions:
            explosion.draw(screen)

    def update(self, left, right, asteroids):
        result = False
        if left:
            self.x_velocity += -3

        if right:
            self.x_velocity += 3

        if not (left or right):
            self.x_velocity = 0

        for asteroid in asteroids:
            if self.rect.colliderect(asteroid.rect):
                self.life -= 1
                rx = random.randint(-20, 20)
                ry = random.randint(-20, 20)
                explosion = Explosion(self.rect.x + rx, self.rect.y + ry)
                self.explosions.append(explosion)
                result = True

        self.rect.x += self.x_velocity
        return result
