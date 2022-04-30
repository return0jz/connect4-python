from constants import *
import numpy
from math import floor

def init_board():
    return numpy.zeros((7, 6))

def draw_board(red_checker, yellow_checker, screen, board):
    for i in range(0, 7):
        for j in range(0, 6):
            if board[i][j] == 1:
                red_checker.draw(screen, (i*SLOT_LENGTH, j*SLOT_LENGTH))
            elif board[i][j] == 2:
                yellow_checker.draw(screen, (i*SLOT_LENGTH, j*SLOT_LENGTH))
                
def drop_slot(board, counters, turn, column):
    counters[column] += 1
    if counters[column] <= 6:
        board[column][6-counters[column]] = 1 if turn else 2
                
def is_won(board): # 0 : none, 1 : red, 2: yellow
    for x in range(0,4):
        for y in range(0,6):
            if (board[x][y] == 1) and (board[x+1][y] == 1) and (board[x+2][y] == 1) and (board[x+3][y] == 1):
                return 1
            elif (board[x][y] == 2) and (board[x+1][y] == 2) and (board[x+2][y] == 2) and (board[x+3][y] == 2):
                return 2
    for x in range(0, 7):
        for y in range(0, 3):
            if (board[x][y] == 1) and (board[x][y+1] == 1) and (board[x][y+2] == 1) and (board[x][y+3] == 1):
                return 1
            elif (board[x][y] == 2) and (board[x][y+1] == 2) and (board[x][y+2] == 2) and (board[x][y+3] == 2):
                return 2
    for x in range(3, 7):
        for y in range(0, 3):
            if (board[x][y] == 1) and (board[x-1][y+1] == 1) and (board[x-2][y+2] == 1) and (board[x-3][y+3] == 1):
                return 1
            if (board[x][y] == 2) and (board[x-1][y+1] == 2) and (board[x-2][y+2] == 2) and (board[x-3][y+3] == 2):
                return 2
    for x in range(0, 4):
        for y in range(0, 3):
            if (board[x][y] == 1) and (board[x+1][y+1] == 1) and (board[x+2][y+2] == 1) and (board[x+3][y+3] == 1):
                return 1
            if (board[x][y] == 2) and (board[x+1][y+1] == 2) and (board[x+2][y+2] == 2) and (board[x+3][y+3] == 2):
                return 2
    return 0 
            
        