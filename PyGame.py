from pygame.locals import *
import Board
import EasyMode
from UIFunctions import *
import ScoreBoard

# General settings
pygame.init()
FPS = 150
FramePerSec = pygame.time.Clock()

# Screen information
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("TicTacToe")


# Creating the board
b = Board.board()
board = pygame.Surface((BOARD_SIZE, BOARD_SIZE))
board.fill(BOARD_COLOR)

Lseperator = pygame.Surface((DELIMITER, BOARD_SIZE-2*BEAUTY_TAX))
Lseperator.fill(SEPERATOR)
Rseperator = pygame.Surface((DELIMITER, BOARD_SIZE-2*BEAUTY_TAX))
Rseperator.fill(SEPERATOR)
Useperator = pygame.Surface((BOARD_SIZE-2*BEAUTY_TAX, DELIMITER))
Useperator.fill(SEPERATOR)
Dseperator = pygame.Surface((BOARD_SIZE-2*BEAUTY_TAX, DELIMITER))
Dseperator.fill(SEPERATOR)

# New game Button
newGame = pygame.Surface((NEW_WIDTH, NEW_HEIGHT))
newGame.fill(NEW_COLOR)
font = pygame.font.SysFont("calibri", NEW_HEIGHT)
newGameTxt = font.render('New Game', True, D_GREY)

# Score Board
score = ScoreBoard.scoreBoard()
font = pygame.font.SysFont("calibri", FONTSIZE)
playerTxt = font.render('Player', True, BLACK)
computerTxt = font.render('Computer', True, BLACK)

# Variables for the program
mouseBox = [-1,-1]
prevMouseBox = [-1,-1]
gameDone = False

# Running the game until interruption
while True:
    # Draw the screen
    screen.fill(SCREEN_COLOR)

    for event in pygame.event.get():
        # Check for quit interaction
        if event.type == QUIT:
            EndGame()


        # Hover
        prevMouseBox = mouseBox
        mouseBox = mouseToBox(pygame.mouse.get_pos())

        if mouseBox != [-1,-1] and b.checkValidMove("x", mouseBox[0], mouseBox[1]) and not gameDone:
            shaded = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
            shaded.fill(D_SHADE)
            board.blit(shaded, boxToLocationBoard(mouseBox[0], mouseBox[1]))


        # The game logic - Upon Click
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mouseBox != [-1, -1] and b.checkValidMove("x", mouseBox[0], mouseBox[1]) and not gameDone:
                b.makeMove("x", mouseBox[0], mouseBox[1])

                # Un-hover the square after move
                normalBox = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
                normalBox.fill(BOARD_COLOR)
                board.blit(normalBox, boxToLocationBoard(prevMouseBox[0], prevMouseBox[1]))

                if b.hasWon("x"):
                    print("x won! congrats!")
                    gameDone = True
                    score.increment("x")
                if b.checkTie():
                    print("Tie! good game!")
                    gameDone = True

                if not gameDone:
                    aiMove = EasyMode.play(b, "o")
                    b.makeMove("o", aiMove[0], aiMove[1])
                    if b.hasWon("o"):
                        print("o won! congrats!")
                        gameDone = True
                        score.increment("o")
                    if b.checkTie():
                        print("Tie! good game!")
                        gameDone = True

    # Draw the board
    screen.blit(board, (SIDE_GAP, VERTICAL_GAP))
    screen.blit(Lseperator, (SIDE_GAP+BEAUTY_TAX+SQUARE_SIZE, VERTICAL_GAP+BEAUTY_TAX))
    screen.blit(Rseperator, (SIDE_GAP+BEAUTY_TAX+2*SQUARE_SIZE+DELIMITER, VERTICAL_GAP+BEAUTY_TAX))
    screen.blit(Useperator, (SIDE_GAP+BEAUTY_TAX,VERTICAL_GAP+BEAUTY_TAX+SQUARE_SIZE))
    screen.blit(Dseperator, (SIDE_GAP+BEAUTY_TAX, VERTICAL_GAP+BEAUTY_TAX+2*SQUARE_SIZE+DELIMITER))


    # Un-hover
    if mouseBox != prevMouseBox and prevMouseBox != [-1,-1]:
        normalBox = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
        normalBox.fill(BOARD_COLOR)
        board.blit(normalBox, boxToLocationBoard(prevMouseBox[0], prevMouseBox[1]))

    # Draw x's and o's
    for row in range(3):
        for col in range(3):
            if b.board[row][col] == '-':
                continue
            if b.board[row][col] == 'x':
                toDraw = pygame.image.load("player.png").convert_alpha()
            if b.board[row][col] == 'o':
                toDraw = pygame.image.load("enemy.png").convert_alpha()

            toDraw = pygame.transform.smoothscale(toDraw, (SQUARE_SIZE, SQUARE_SIZE))

            board.blit(toDraw, boxToLocationBoard(row, col))

    # Draw new-game Button
    screen.blit(newGame, ( (SCREEN_WIDTH - NEW_WIDTH)/2, (SCREEN_HEIGHT + BOARD_SIZE- NEW_HEIGHT) / 2))
    newGame.blit(newGameTxt, (5,2))

    if event.type == pygame.MOUSEBUTTONDOWN and onNewGame(pygame.mouse.get_pos()):
        b.emptyBoard()
        board.fill(BOARD_COLOR)
        for row in range(3):
            for col in range(3):
                pygame.Surface((BOARD_SIZE, BOARD_SIZE))
        gameDone = False

    # Draw Score Board
    screen.blit(playerTxt, (PLAYER_WIDTH, PLAYER_HEIGHT))
    playrScore = font.render(str(score.x_score), True, BLACK)
    screen.blit(playrScore, (PLAYER_WIDTH + 12, PLAYER_HEIGHT + 15))

    screen.blit(computerTxt, (COMPUTER_WIDTH, COMPUTER_HEIGHT))
    computerScore = font.render(str(score.o_score), True, BLACK)
    screen.blit(computerScore, (COMPUTER_WIDTH + 25, COMPUTER_HEIGHT + 15))

    # Update the game at each iteration
    pygame.display.update()
    FramePerSec.tick(FPS)




