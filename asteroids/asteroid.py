import pygame
from pygame.transform import scale


class Asteroid(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = scale(pygame.image.load("images/asteroid.png"), (50, 50))
        self.rect = pygame.Rect(x, y, 50, 50)
        self.yvel = 5

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        self.rect.y += self.yvel

        if self.rect.y > 900:
            self.kill()