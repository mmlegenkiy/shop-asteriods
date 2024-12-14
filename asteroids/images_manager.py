import pygame
from pygame.transform import scale

class ImagesManager:
    def __init__(self):
        self.background = pygame.image.load("images/background.jpg")
        sky = scale(big_sky, (800, 600))