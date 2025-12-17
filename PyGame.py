import pygame
from pygame.locals import *
from sys import exit
import Board
import EasyMode

def clickToPos(pos):
    x = -1
    y = -1

    # Assign x value
    if SIDE_GAP+BEAUTY_TAX < pos[0] < SIDE_GAP+BEAUTY_TAX+SQUARE_SIZE:
        x = 0
    elif SIDE_GAP+BEAUTY_TAX+SQUARE_SIZE+DELIMITER < pos[0] < SIDE_GAP+BEAUTY_TAX+2*SQUARE_SIZE+DELIMITER:
        x = 1
    elif SIDE_GAP+BEAUTY_TAX+2*SQUARE_SIZE+2*DELIMITER < pos[0] < SIDE_GAP+BEAUTY_TAX+3*SQUARE_SIZE+2*DELIMITER:
        x = 2

    # Assign y value
    if VERTICAL_GAP + BEAUTY_TAX < pos[1] < VERTICAL_GAP + BEAUTY_TAX + SQUARE_SIZE:
        y = 0
    elif VERTICAL_GAP+BEAUTY_TAX+SQUARE_SIZE+DELIMITER < pos[1] < VERTICAL_GAP+BEAUTY_TAX+2*SQUARE_SIZE+DELIMITER:
        y = 1
    elif VERTICAL_GAP+BEAUTY_TAX+2*SQUARE_SIZE+2*DELIMITER < pos[1] < VERTICAL_GAP+BEAUTY_TAX+3*SQUARE_SIZE+2*DELIMITER:
        y = 2

    # Both good or none
    if x != -1 and y != -1:
        return x, y
    return [-1,-1]

def EndGame():
    pygame.quit()
    exit()

def draw(b, x, y):
    if b.board[x][y] == 'x':
        toDraw = pygame.image.load("player.png").convert_alpha()
    else:
        toDraw = pygame.image.load("enemy.png").convert_alpha()
    toDraw = pygame.transform.smoothscale(toDraw, (SQUARE_SIZE, SQUARE_SIZE))

    location = boxToLocation(x,y)
    screen.blit(toDraw, location)

def boxToLocation(x,y):
    match x, y:
        case 0, 0:
            return SIDE_GAP+BEAUTY_TAX, VERTICAL_GAP+BEAUTY_TAX
        case 1, 0:
            return SIDE_GAP+BEAUTY_TAX+SQUARE_SIZE+DELIMITER, VERTICAL_GAP+BEAUTY_TAX
        case 2, 0:
            return SIDE_GAP+BEAUTY_TAX+2*SQUARE_SIZE+2*DELIMITER, VERTICAL_GAP+BEAUTY_TAX
        case 0, 1:
            return SIDE_GAP+BEAUTY_TAX, VERTICAL_GAP+BEAUTY_TAX+SQUARE_SIZE+DELIMITER
        case 1, 1:
            return SIDE_GAP+BEAUTY_TAX+SQUARE_SIZE+DELIMITER, VERTICAL_GAP+BEAUTY_TAX+SQUARE_SIZE+DELIMITER
        case 2, 1:
            return SIDE_GAP+BEAUTY_TAX+2*SQUARE_SIZE+2*DELIMITER, VERTICAL_GAP+BEAUTY_TAX+SQUARE_SIZE+DELIMITER
        case 0, 2:
            return SIDE_GAP+BEAUTY_TAX, VERTICAL_GAP+BEAUTY_TAX+2*SQUARE_SIZE+2*DELIMITER
        case 1, 2:
            return SIDE_GAP+BEAUTY_TAX+SQUARE_SIZE+DELIMITER, VERTICAL_GAP+BEAUTY_TAX+2*SQUARE_SIZE+2*DELIMITER
        case 2, 2:
            return SIDE_GAP+BEAUTY_TAX+2*SQUARE_SIZE+2*DELIMITER, VERTICAL_GAP+BEAUTY_TAX+2*SQUARE_SIZE+2*DELIMITER
        case _:
            return -1, -1


# General settings
pygame.init()
FPS = 60
FramePerSec = pygame.time.Clock()

# Predefined some colors
BLUE = (100, 100, 250)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
L_GREY = (222, 222, 222)
SEPERATOR = (50,50,200)

# Screen information
SQUARE_SIZE = 100
SIDE_GAP = 20
VERTICAL_GAP = 10
DELIMITER = 5
BEAUTY_TAX = 10
SCREEN_WIDTH = 2 * (SIDE_GAP+BEAUTY_TAX+DELIMITER+1.5*SQUARE_SIZE)
SCREEN_HEIGHT = 2 * (3*VERTICAL_GAP+BEAUTY_TAX+1.5*SQUARE_SIZE+DELIMITER)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("TicTacToe")
SCREEN_COLOR = WHITE

BOARD_SIZE = SCREEN_WIDTH - 2 * SIDE_GAP

# Creating the board
b = Board.board()
board = pygame.Surface((BOARD_SIZE, BOARD_SIZE))
board.fill(BLUE)

Lseperator = pygame.Surface((DELIMITER, BOARD_SIZE-2*BEAUTY_TAX))
Lseperator.fill(SEPERATOR)
Rseperator = pygame.Surface((DELIMITER, BOARD_SIZE-2*BEAUTY_TAX))
Rseperator.fill(SEPERATOR)
Useperator = pygame.Surface((BOARD_SIZE-2*BEAUTY_TAX, DELIMITER))
Useperator.fill(SEPERATOR)
Dseperator = pygame.Surface((BOARD_SIZE-2*BEAUTY_TAX, DELIMITER))
Dseperator.fill(SEPERATOR)


# Running the game until interruption
while True:
    # Draw the screen
    screen.fill(SCREEN_COLOR)

    for event in pygame.event.get():
        # Check for quit interaction
        if event.type == QUIT:
            EndGame()

        # Upon click - if QUIT exit, else check if legal move and play
        if event.type == pygame.MOUSEBUTTONDOWN:
            box = clickToPos(pygame.mouse.get_pos())
            if box != [-1, -1]:
                b.makeMove("x", box[0], box[1])
                if b.hasWon("x"):
                    print("x won! congrats!")
                    EndGame()
                if b.checkTie():
                    print("Tie! good game!")
                    EndGame()

                aiMove = EasyMode.play(b, "o")
                b.makeMove("o", aiMove[0], aiMove[1])
                if b.hasWon("o"):
                    print("o won! congrats!")
                    EndGame()
                if b.checkTie():
                    print("Tie! good game!")
                    EndGame()

    # Draw the board
    screen.blit(board, (SIDE_GAP, VERTICAL_GAP))
    screen.blit(Lseperator, (SIDE_GAP+BEAUTY_TAX+SQUARE_SIZE, VERTICAL_GAP+BEAUTY_TAX))
    screen.blit(Rseperator, (SIDE_GAP+BEAUTY_TAX+2*SQUARE_SIZE+DELIMITER, VERTICAL_GAP+BEAUTY_TAX))
    screen.blit(Useperator, (SIDE_GAP+BEAUTY_TAX,VERTICAL_GAP+BEAUTY_TAX+SQUARE_SIZE))
    screen.blit(Dseperator, (SIDE_GAP+BEAUTY_TAX, VERTICAL_GAP+BEAUTY_TAX+2*SQUARE_SIZE+DELIMITER))

    # Draw x's and o's
    for i in range(3):
        for j in range(3):
            if b.board[i][j] != '-':
                draw(b, i, j)

    # Update the game at each iteration
    pygame.display.update()
    FramePerSec.tick(FPS)




