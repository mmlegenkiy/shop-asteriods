import pygame
from pygame.transform import scale


class SpaceObject(pygame.sprite.Sprite):
    """
    Клас космічний об'єкт, що наслідується від класу pygame.sprite.Sprite. Реалізовано
    методи draw та update, які у класах нащадках будуть використовуватись або модифіковуватись
    """
    def __init__(self, x_position, y_position):
        """
        Створює об'єкт для застосування до нього методів draw та update
        :param x_position: положення космічного об'єкта по горизонталі, ціле число
        :param y_position: положення космічного об'єкта по вертикалі, ціле число
        """
        pygame.sprite.Sprite.__init__(self)
        self.width = 1
        self.height = 1
        self.rect = pygame.Rect(x_position, y_position, self.width, self.height)
        self.image = scale(pygame.image.load("images/background.jpg"), (self.width, self.height))
        self.x_velocity = 0
        self.y_velocity = 0

    def draw(self, screen):
        """
        Малює об'єкт на екрані
        :param screen: вікно для малювання
        """
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        """
        Змінює положення об'єкта у просторі, використовуючи швидкість
        """
        self.rect.x += self.x_velocity
        self.rect.y += self.y_velocity
