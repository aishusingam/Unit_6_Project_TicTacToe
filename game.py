class Board:

    def __init__(self):
        self.positions = [' '] * 10


    def printBoard(self):
        # "board" is a list of 10 strings representing the board (ignore index 0)
        print('   |   |')
        print(' ' + self.positions[7] + ' | ' + self.positions[8] + ' | ' + self.positions[9])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.positions[4] + ' | ' + self.positions[5] + ' | ' + self.positions[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.positions[1] + ' | ' + self.positions[2] + ' | ' + self.positions[3])
        print('   |   |')


    def checkOpenPos(self, i):
        return self.positions[i] == ' '

    # Check if any 3 in a row have that specific symbol
    # In order, we check for
    # Top 3, Middle 3, Bottom 3
    # Left 3, Middle 3, Right 3
    # Left Diagonal, Right Diagonal
    def isWon(self, sym):

        return ((self.positions[7] == sym and self.positions[8] == sym and self.positions[9] == sym) or
        (self.positions[4] == sym and self.positions[5] == sym and self.positions[6] == sym) or
        (self.positions[1] == sym and self.positions[2] == sym and self.positions[3] == sym) or
        (self.positions[7] == sym and self.positions[4] == sym and self.positions[1] == sym) or
        (self.positions[8] == sym and self.positions[5] == sym and self.positions[2] == sym) or
        (self.positions[9] == sym and self.positions[6] == sym and self.positions[3] == sym) or
        (self.positions[7] == sym and self.positions[5] == sym and self.positions[3] == sym) or
        (self.positions[9] == sym and self.positions[5] == sym and self.positions[1] == sym))

    # Checks if the board is filled
    def fullBoard(self):
        for i in range(1,10):
            if checkOpenPos(i):
                return False
        return True

    # Checks if there is a final tie or if the game is to keep going
    def tie(self, sym1, sym2):
        return fullBoard() and not isWon(sym1) and not isWon(sym2)


class Player:

    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    # Pass position i and Board object b
    def makeMove(self, i, b):
        b.positions[i] = self.symbol



# Testing
p1 = Player("First", 'x')
p2 = Player("Second", 'o')
board = Board()

p1.makeMove(1, board)
print(board.printBoard())
print()
p2.makeMove(5, board)
print(board.printBoard())
