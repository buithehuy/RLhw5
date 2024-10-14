import random

class Teacher:
    """ 
    A class to implement a teacher that knows the optimal playing strategy.
    Teacher returns the best move at any time given the current state of the game.

    Parameters
    ----------
    level : float 
        teacher ability level. This is a value between 0-1 that indicates the
        probability of making the optimal move at any given time.
    """

    def __init__(self, level=0.9):
        self.ability_level = level

    def win(self, board, key='X'):
        """ If we have three in a row and the 4th is available, take it. """
        # Check diagonal wins
        a = [board[i][i] for i in range(4)]
        b = [board[i][3 - i] for i in range(4)]
        if a.count('-') == 1 and a.count(key) == 3:
            ind = a.index('-')
            return ind, ind
        elif b.count('-') == 1 and b.count(key) == 3:
            ind = b.index('-')
            return ind, 3 - ind

        # Check rows and columns
        for i in range(4):
            row = [board[i][j] for j in range(4)]
            col = [board[j][i] for j in range(4)]
            if row.count('-') == 1 and row.count(key) == 3:
                return i, row.index('-')
            elif col.count('-') == 1 and col.count(key) == 3:
                return col.index('-'), i
        return None

    def blockWin(self, board):
        """ Block the opponent if they have a win available. """
        return self.win(board, key='O')

    def fork(self, board):
        """ Create a fork opportunity such that we have multiple threats to win. """
        # For 4x4, it's a bit more complex but we can focus on center and adjacent pairs
        for i in range(3):
            for j in range(3):
                if board[i][j] == 'X' and board[i+1][j+1] == 'X':
                    if board[i][j+1] == '-' and board[i+1][j] == '-':
                        return i, j+1
        return None

    def blockFork(self, board):
        """ Block the opponent's fork if they have one available. """
        return self.fork(board)

    def center(self, board):
        """ Pick the center if it is available. """
        if board[1][1] == '-':
            return 1, 1
        return None

    def corner(self, board):
        """ Pick a corner move. """
        if board[0][0] == '-':
            return 0, 0
        elif board[0][3] == '-':
            return 0, 3
        elif board[3][0] == '-':
            return 3, 0
        elif board[3][3] == '-':
            return 3, 3
        return None

    def sideEmpty(self, board):
        """ Pick an empty side. """
        sides = [(0, 1), (0, 2), (1, 0), (1, 3), (2, 0), (2, 3), (3, 1), (3, 2)]
        for (i, j) in sides:
            if board[i][j] == '-':
                return i, j
        return None

    def randomMove(self, board):
        """ Choose a random move from the available options. """
        possibles = [(i, j) for i in range(4) for j in range(4) if board[i][j] == '-']
        return possibles[random.randint(0, len(possibles)-1)]

    def makeMove(self, board):
        """
        Trainer goes through a hierarchy of moves, making the best move that
        is currently available each time. A tuple is returned that represents
        (row, col).
        """
        if random.random() > self.ability_level:
            return self.randomMove(board)
        
        a = self.win(board)
        if a is not None:
            return a
        a = self.blockWin(board)
        if a is not None:
            return a
        a = self.fork(board)
        if a is not None:
            return a
        a = self.blockFork(board)
        if a is not None:
            return a
        a = self.center(board)
        if a is not None:
            return a
        a = self.corner(board)
        if a is not None:
            return a
        a = self.sideEmpty(board)
        if a is not None:
            return a
        return self.randomMove(board)
