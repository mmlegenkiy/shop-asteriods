import pygame
import random
from pygame.transform import scale
from explosion import Explosion
from space_object import SpaceObject


class Spaceship(SpaceObject):
    """
    Клас космічний корабель. Наслідується від класу космічний об'єкт, модифікує атрибути та методи батьківського класу,
    додає нові атрибути та методи.
    """
    def __init__(self, x_position, y_position):
        """
        Ініціалізатор батьківського класу доповнено властивостями космічного корабля, зокрема додано життя та
        створюються вибухи у випадку перетину із астероїдами
        :param x_position: положення космічного корабля по горизонталі, ціле число
        :param y_position: положення космічного корабля по вертикалі, ціле число
        """
        super().__init__(x_position, y_position)
        self.width = 50
        self.height = 100
        self.rect = pygame.Rect(x_position, y_position, self.width, self.height)
        self.image = scale(pygame.image.load("images/ship.png"), (self.width, self.height))
        self.life = 100
        self.explosions = []

    def draw(self, screen):
        """
        Викликається метод draw із батьківського класу та малюються вибухи у випадку їх наявності
        :param screen: вікно, на якому малюється об'єкт
        """
        super().draw(screen)
        for explosion in self.explosions:
            explosion.draw(screen)

    def change_velocity(self, left, right):
        """
        Метод для зміни швидкості корабля, викликається в класі Гра та передає інформацію
        про натиснуті (чи відпущені) користувачем клавіші
        :param left: логічна змінна, показує, чи треба рухатись ліворуч
        :param right: логічна змінна, показує, чи треба рухатись праворуч
        """
        if left:
            self.x_velocity += -3
        if right:
            self.x_velocity += 3
        if not (left or right):
            self.x_velocity = 0

    def check_collisions(self, asteroids):
        """
        Метод для пошуку перетину космічного корабля із астероїдами. Якщо перетин трапляється,
        то у випадковій точці поблизу корабля створюється вибух та зменшується кількість життів.
        :param asteroids: список об'єктів астероїдів, для яких треба здійснити перевірку на перетин
        :return: логічна змінна, за наявності хоч одного перетину повертається True, інакше - False
        """
        for asteroid in asteroids:
            if self.rect.colliderect(asteroid.rect):
                self.life -= 1
                rx = random.randint(-20, 20)
                ry = random.randint(-20, 20)
                explosion = Explosion(self.rect.x + rx, self.rect.y + ry)
                self.explosions.append(explosion)
                return True
        else:
            return False

    def move(self, width):
        """
        Метод для руху корабля. Використовує метод update батьківського класу. Забороняє рух
        (скидає координату до граничного значення) за спроби вийти за межі екрану.
        :param width: ширина екрану, ціле число
        """
        super().update()
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > width - self.width:
            self.rect.x = width - self.width
