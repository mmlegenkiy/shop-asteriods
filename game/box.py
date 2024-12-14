import pygame


class Box:
    def __init__(self, x_position, y_position, size, color):
        self.x_position = x_position
        self.y_position = y_position
        self.size = size
        self.color = color
        self.rectangle = pygame.Rect(self.x_position, self.y_position, self.size, self.size)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rectangle)
