from Constants import *
import pygame


def mouseToBox(pos):
    x = -1
    y = -1

    # Assign y value
    if SIDE_GAP + BEAUTY_TAX < pos[0] < SIDE_GAP + BEAUTY_TAX + SQUARE_SIZE:
        y = 0
    elif SIDE_GAP + BEAUTY_TAX + SQUARE_SIZE + DELIMITER < pos[0] < SIDE_GAP + BEAUTY_TAX + 2 * SQUARE_SIZE + DELIMITER:
        y = 1
    elif SIDE_GAP + BEAUTY_TAX + 2 * SQUARE_SIZE + 2 * DELIMITER < pos[
        0] < SIDE_GAP + BEAUTY_TAX + 3 * SQUARE_SIZE + 2 * DELIMITER:
        y = 2

    # Assign x value
    if VERTICAL_GAP + BEAUTY_TAX < pos[1] < VERTICAL_GAP + BEAUTY_TAX + SQUARE_SIZE:
        x = 0
    elif VERTICAL_GAP + BEAUTY_TAX + SQUARE_SIZE + DELIMITER < pos[
        1] < VERTICAL_GAP + BEAUTY_TAX + 2 * SQUARE_SIZE + DELIMITER:
        x = 1
    elif VERTICAL_GAP + BEAUTY_TAX + 2 * SQUARE_SIZE + 2 * DELIMITER < pos[
        1] < VERTICAL_GAP + BEAUTY_TAX + 3 * SQUARE_SIZE + 2 * DELIMITER:
        x = 2

    # Both good or none
    if x != -1 and y != -1:
        return x, y
    return [-1, -1]


def EndGame():
    pygame.quit()
    exit()


def draw(b, x, y):
    if b.board[x][y] == 'x':
        toDraw = pygame.image.load("player.png").convert_alpha()
    else:
        toDraw = pygame.image.load("enemy.png").convert_alpha()
    toDraw = pygame.transform.smoothscale(toDraw, (SQUARE_SIZE, SQUARE_SIZE))

    location = boxToLocationScreen(x, y)
    return toDraw, location


def boxToLocationScreen(x, y):
    if x in [0, 1, 2] and y in [0, 1, 2]:
        return SIDE_GAP + BEAUTY_TAX + x * (SQUARE_SIZE + DELIMITER), VERTICAL_GAP + BEAUTY_TAX + y * (
                    SQUARE_SIZE + DELIMITER)

    else:
        return -1, -1


def boxToLocationBoard(x, y):
    if x in [0, 1, 2] and y in [0, 1, 2]:
        return y * (SQUARE_SIZE + DELIMITER) + BEAUTY_TAX, x * (SQUARE_SIZE + DELIMITER) + BEAUTY_TAX,

    else:
        return -1, -1


def onNewGame(mouseLocation):
    wide_min = (SCREEN_WIDTH - NEW_WIDTH) / 2
    height_min = (SCREEN_HEIGHT + BOARD_SIZE - NEW_HEIGHT) / 2
    if wide_min < mouseLocation[0] < wide_min + NEW_WIDTH and height_min < mouseLocation[1] < height_min + NEW_HEIGHT:
        return True
