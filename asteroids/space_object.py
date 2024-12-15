import pygame
from pygame.transform import scale


class SpaceObject(pygame.sprite.Sprite):
    def __init__(self, x_position, y_position):
        pygame.sprite.Sprite.__init__(self)
        self.width = 1
        self.height = 1
        self.rect = pygame.Rect(x_position, y_position, self.width, self.height)
        self.image = scale(pygame.image.load(""), (self.width, self.height))

    # class Spaceship(pygame.sprite.Sprite):
    #     def __init__(self, x, y):
    #         pygame.sprite.Sprite.__init__(self)
    #         self.rect = pygame.Rect(x, y, 50, 100)
    #         self.image = scale(pygame.image.load("images/ship.png"), (50, 100))
    #         self.xvel = 0
    #         # добавим кораблю здоровье
    #         self.life = 100
    #         self.explosions = []
    #
    #     def draw(self, screen):
    #         # print(self.rect.x)
    #         screen.blit(self.image, (self.rect.x, self.rect.y))
    #         for explosion in self.explosions:
    #             explosion.draw(screen)
    #
    #     def update(self, left, right, asteroids):
    #         result = False
    #         if left:
    #             self.xvel += -3
    #
    #         if right:
    #             self.xvel += 3
    #
    #         if not (left or right):
    #             self.xvel = 0
    #
    #         for asteroid in asteroids:
    #             if self.rect.colliderect(asteroid.rect):
    #                 self.life -= 1
    #                 rx = random.randint(-5, 40)
    #                 ry = random.randint(-5, 40)
    #                 explosion = Explosion(self.rect.x + rx, self.rect.y + ry)
    #                 self.explosions.append(explosion)
    #                 result = True
    #
    #         self.rect.x += self.xvel
    #         return result
    #     # def update(self, left, right):
    #     #     if left:
    #     #         self.xvel -= 3
    #     #     if right:
    #     #         self.xvel += 3
    #     #     if not (left or right):
    #     #         self.xvel = 0
    #     #     self.rect.x += self.xvel
