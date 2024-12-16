import pygame
from pygame.transform import scale
from space_object import SpaceObject


class Explosion(SpaceObject):
    """
    Клас вибух. Використовує та наслідує із батьківського класу.
    """
    def __init__(self, x_position, y_position):
        """
        Ініціалізатор батьківського класу доповнено властивостями вибуха. Зокрема, реалізовано зміну картинки з плином часу.
        :param x_position: положення вибуха по горизонталі, ціле число
        :param y_position: положення вибуха по вертикалі, ціле число
        """
        super().__init__(x_position, y_position)
        self.width = 40
        self.height = 40
        self.rect = pygame.Rect(x_position, y_position, self.width, self.height)
        self.images = []
        self.number_images = 8
        for i in range(self.number_images):
            image = scale(pygame.image.load(f"images/explosion/tile{i}.png"), (self.width, self.height))
            self.images.append(image)
        self.index = 0
        self.image = self.images[self.index]

    def draw(self, screen):
        """
        Модифікує метод draw для батьківського класу: змінює картинку з плином часу.
        Після того, як показано всі картинки вибуху на різних стадіях, більше нічого не малюється.
        :param screen: вікно, на якому малюється об'єкт
        """
        if self.index < self.number_images - 1:
            super().draw(screen)
            self.index += 1
        self.image = self.images[self.index]
