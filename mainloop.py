from constants import SCREEN_HEIGHT, SCREEN_WIDTH, SLOT_LENGTH
from gfx import Sprite
import pygame
from logic import draw_board, init_board, drop_slot, is_won
from math import floor    

class Mainloop:
    def __init__(self):
        self.red_checker = Sprite("res/red.png", (SLOT_LENGTH + 20, SLOT_LENGTH)) # + 20 to stretch
        self.yellow_checker = Sprite("res/yellow.png", (SLOT_LENGTH, SLOT_LENGTH))
        self.foreground = Sprite("res/fg.png", (SCREEN_WIDTH, SCREEN_HEIGHT + 130)) # + 130 to stretch
        self.font_surface = pygame.font.SysFont('Comic Sans', 30)
        
        self.is_dropping = False # animation is playing
        
        self.game_over = False # 
        self.is_draw = False
        
        self.turn = True # True : red, False : yellow
        self.board = init_board()
        self.counters = [0]*7
        
    def handle_event(self, e):
        if e.type == pygame.MOUSEBUTTONUP:
            if self.game_over:
                self.game_over = False
                self.board = init_board()     
                self.counters = [0]*7
                self.turn = True          
            elif not self.is_dropping:
                column = floor(pygame.mouse.get_pos()[0]/SLOT_LENGTH)
                self.is_dropping = True
                self.anim_sprite_color = self.turn
                self.anim_sprite_column = column
                self.anim_sprite_endpos = self.counters[column] + 1
                self.anim_sprite_y = 0
                self.anim_sprite_speed = 100
    def update(self, dt):
        if self.is_dropping:
            self.anim_sprite_speed += 500 * dt # px / second
            self.anim_sprite_y += self.anim_sprite_speed * dt # px / second^2
            if self.anim_sprite_y >= SLOT_LENGTH * (6 - self.anim_sprite_endpos): # if reach endpos, cut animation and mutate board
                drop_slot(self.board, self.counters, self.turn, self.anim_sprite_column)
                self.is_dropping = False
                self.turn = not self.turn
                if is_won(self.board):
                    self.game_over = True
                else:
                    is_full = True # flag for if all spots on board is filled
                    for i in range(0, 7):
                        for j in self.board[i]:
                            if j == 0:
                                is_full = False
                    if is_full:
                        self.game_over = True
                        self.is_draw == True
    def draw(self, screen):
        if self.is_dropping:
            (self.red_checker if self.anim_sprite_color else self.yellow_checker).draw(screen, (self.anim_sprite_column * SLOT_LENGTH, self.anim_sprite_y))        
        draw_board(self.red_checker, self.yellow_checker, screen, self.board)
        self.foreground.draw(screen, (0,0))
        if self.game_over:
            if self.is_draw:
                text = self.font_surface.render("It's a draw! Click to play again.", True, (255, 255, 255))
            else:
                text = self.font_surface.render(("Red" if not self.turn else "Yellow") + " won! Click to play again.", True, (255, 255, 255)) # if NOT because turn switches after player wins
            text_rect = text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
            screen.blit(text, text_rect)