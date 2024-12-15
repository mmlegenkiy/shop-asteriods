import pygame
from pygame.transform import scale


class Asteroid(pygame.sprite.Sprite):
    def __init__(self, x_position, y_position):
        pygame.sprite.Sprite.__init__(self)
        self.width = 50
        self.height = 50
        self.image = scale(pygame.image.load("images/asteroid.png"), (self.width, self.height))
        self.rect = pygame.Rect(x_position, y_position, self.width, self.height)
        self.x_velocity = 0
        self.y_velocity = 5

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self, sizes):
        self.rect.y += self.y_velocity
        self.rect.y += self.x_velocity

        if self.rect.x > sizes[0] or self.rect.x < 0:
            self.kill()
        if self.rect.y > sizes[1] or self.rect.y < 0:
            self.kill()
