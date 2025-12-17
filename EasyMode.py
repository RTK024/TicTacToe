import random

def canIWin(board, me):
    """
    :param board: game board
    :param me: the type of player "x" or "o"
    :return: [col, row] to play if win is possible, [-1, -1] if not
    """
    if me not in ["x", "o"]:
        print("Enter viable player")
        exit(0)

    otherPlayer = "x" if me == "o" else "o"

    # Check row win
    for row in range(3):
        count = 0
        emptyLocation = -1
        for col in range(3):
            if board.board[row][col] == otherPlayer:
                count = 0
                break
            if board.board[row][col] == me:
                count += 1
            else:
                emptyLocation = col

        if count == 2 and emptyLocation != -1:
            return [row, emptyLocation]

    # Check col win
    for col in range(3):
        count = 0
        emptyLocation = -1
        for row in range(3):
            if board.board[row][col] == otherPlayer:
                count = 0
                break
            if board.board[row][col] == me:
                count += 1
            else:
                emptyLocation = row

        if count == 2 and emptyLocation != -1:
            return [emptyLocation, col]

    # Check left diag win
    count = 0
    emptyLocation = -1
    for i in range(3):
        if board.board[i][i] == otherPlayer:
            break
        if board.board[i][i] == me:
            count += 1
        else:
            emptyLocation = i

    if count == 2:
        return [emptyLocation, emptyLocation]

    # Check right diag win
    count = 0
    emptyLocation = -1
    for i in range(3):

        if board.board[i][2-i] == otherPlayer:
            break
        if board.board[i][2-i] == me:
            count += 1
        else:
            emptyLocation = i

    if count == 2:
        return [emptyLocation, 2-emptyLocation]

    return [-1, -1]



def needIBlock(board, me):
    """
    :param board: game board
    :param me: the type of player "x" or "o"
    :return: if other player can win returns how to block if not return [-1,-1]
    """
    if me not in ["x", "o"]:
        print("Enter viable player")
        exit(0)

    otherPlayer = "x" if me == "o" else "o"
    return canIWin(board, otherPlayer)

def playRandom(board):
    """
    :param board: game board
    :return: random viable move to play, if none available returns [-1,-1]
    """
    viableMoves = set()

    for row in range(3):
        for col in range(3):
            if board.board[row][col] == "-":
                viableMoves.add((row, col))

    if viableMoves:
        return list(random.choice(list(viableMoves)))
    else:
        return [-1, -1]

def play(boad, me):

    move = canIWin(boad, me)
    if move != [-1,-1]:
        return move

    move = needIBlock(boad, me)
    if move != [-1,-1]:
        return move

    return playRandom(boad)
