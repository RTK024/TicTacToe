class scoreBoard:
    def __init__(self):
        self.x_score = 0
        self.o_score = 0

    def increment(self, player):
        if player not in ['x', 'o']:
            print("Player must be either 'x' or 'o'")
            exit(2)
        if player == 'x':
            self.x_score += 1
        else:
            self.o_score += 1

    def zeroScore(self):
        self.x_score = 0
        self.o_score = 0