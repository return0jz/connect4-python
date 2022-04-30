import pygame
import os

class Sprite:
    def __init__(self, path, height_width):
        self.img = pygame.image.load(os.path.join(path))
        self.img.convert()
        self.img = pygame.transform.scale(self.img, height_width)

    def draw(self, screen, coord):
        screen.blit(self.img, coord)