from game import Board
from game import Player
import random
print('Welcome to Tic Tac Toe!')

player1 = Player("Player 1", 'x')
player2 = Player("player 2", 'o')
board = Board()


def whoGoesFirst():
    # Randomly choose the player who goes first.
    if random.randint(0, 1) == 0:
        return 'player 2'
    else:
        return 'player 1'
def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

while True:
    # Reset the board
    theBoard = [' '] * 10
    turn = whoGoesFirst()
    print(turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player 1':
            # Player 1's turn.
            board.printBoard()
            move = player1.getPlayerMove(board)
            player1.makeMove(move,board)
            if board.isWon(player1.symbol):
                board.printBoard()
                print('Hooray! Player 1 has won the game!')
                gameIsPlaying = False
            else:
                if board.fullBoard():
                    board.printBoard()
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player 2'

        else:
            # Player 2's turn.
            board.printBoard()
            move = player2.getPlayerMove(board)
            player2.makeMove(move, board)

            if board.isWon(player2.symbol):
                board.printBoard()
                print('Hooray! Player 2 has won the game!')
                gameIsPlaying = False
            else:
                if board.fullBoard():
                    board.printBoard()
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player 1'
    board = Board()
    if not playAgain():
        break
