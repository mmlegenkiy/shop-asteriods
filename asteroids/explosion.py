import pygame
from pygame.transform import scale


class Explosion(pygame.sprite.Sprite):
    def __init__(self, x_position, y_position):
        pygame.sprite.Sprite.__init__(self)
        self.width = 40
        self.height = 40
        self.rect = pygame.Rect(x_position, y_position, self.width, self.height)
        self.images = []
        self.index = 0

        for i in range(8):
            image = scale(pygame.image.load(f"images/explosion/tile00{i}.png"), (self.width, self.height))
            self.images.append(image)

    def draw(self, screen):
        if self.index < 8:
            screen.blit(self.images[self.index], (self.rect.x, self.rect.y))
            self.index += 1