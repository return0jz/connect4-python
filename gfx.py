import pygame
import os
from constants import *

class Sprite:
    def __init__(self, path, height_width):
        self.img = pygame.image.load(os.path.join(path))
        self.img.convert()
        self.img = pygame.transform.scale(self.img, height_width)

    def draw(self, screen, coord):
        screen.blit(self.img, coord)
        
def draw_board(red_checker, yellow_checker, screen, board):
    for i in range(0, 7):
        for j in range(0, 6):
            if board[i][j] == 1:
                red_checker.draw(screen, (i*SLOT_LENGTH, j*SLOT_LENGTH))
            elif board[i][j] == 2:
                yellow_checker.draw(screen, (i*SLOT_LENGTH, j*SLOT_LENGTH))