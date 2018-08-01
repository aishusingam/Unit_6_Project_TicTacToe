#class Board
class Board:

    # to initialize the object
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
        #If there is open spot
        return self.positions[i] == ' '

    # Check if any 3 in a row have that specific symbol
    # In order, we check for
    # Top 3, Middle 3, Bottom 3
    # Left 3, Middle 3, Right 3
    # Left Diagonal, Right Diagonal
    def isWon(self, sym):
        # check if the given symbol is won
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
            if self.checkOpenPos(i):
                return False
        return True

    # Checks if there is a final tie or if the game is to keep going
    def tie(self, sym1, sym2):
        return self.fullBoard() and not self.isWon(sym1) and not self.isWon(sym2)

# class Player
class Player:

    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    # Pass position i and Board object b
    def makeMove(self, i, b):
        b.positions[i] = self.symbol

    def getPlayerMove(self, board):
        # Let the player type in his move.
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not board.checkOpenPos(int(move)):
            print('What is your next move, ' + self.name + '? (1-9)')
            move = input()
        return int(move)


# Testing
# p1 = Player("First", 'x')
# p2 = Player("Second", 'o')
# board = Board()
# move = p1.getPlayerMove(board)
# p1.makeMove(move, board)
# print(board.printBoard())
# print()
# move = p2.getPlayerMove(board)
# p2.makeMove(move, board)
# print(board.printBoard())
