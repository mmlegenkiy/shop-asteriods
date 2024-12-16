import pygame
from pygame.transform import scale
from space_object import SpaceObject


class Asteroid(SpaceObject):
    """
    Клас астероід. Наслідується від класу космічний об'єкт, для малювання використовується метод із батьківського класу.
    """
    def __init__(self, x_position, y_position):
        """
        ініціалізатор батьківського класу доповнено властивостями астероїда
        :param x_position: положення астероїда по горизонталі, ціле число
        :param y_position: положення астероїда по вертикалі, ціле число
        """
        super().__init__(x_position, y_position)
        self.width = 50
        self.height = 50
        self.image = scale(pygame.image.load("images/asteroid.png"), (self.width, self.height))
        self.rect = pygame.Rect(x_position, y_position, self.width, self.height)
        self.x_velocity = 0
        self.y_velocity = 5

    def move(self, height):
        """
        Використовує метод update батьківського класу. Додано новий функціонал -
        у випадку, якщо астероїд вилітає вниз за межі екрану він знищується.
        :param height: висота екрану, ціле число
        """
        super().update()
        if self.rect.x > height + self.height:
            self.kill()
