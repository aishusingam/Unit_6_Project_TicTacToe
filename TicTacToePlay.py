#Tic Tac Toe Game Play


#imports Board class from game file.
from game import Board
#mports Player class from game file.
from game import Player
#mports random module.
import random


print('Welcome to Tic Tac Toe!')

#create Player 1 object.
player1 = Player("Player 1", 'x')
#create Player 2 object.
player2 = Player("player 2", 'o')

#create board object.
board = Board()

def whoGoesFirst():
    # randomly choose the player who goes first.
    if random.randint(0, 1) == 0:
        return 'player 2'
    else:
        return 'player 1'

def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

#game starts
while True:
    #select randomly the player.
    turn = whoGoesFirst()
    print(turn + ' will go first.')
    gameIsPlaying = True
    #loop until players are playing the game.
    while gameIsPlaying:
        if turn == 'player 1':
            # Player 1's turn.
            board.printBoard()
            #Player inputs his/her move.
            move = player1.getPlayerMove(board)
            #Make Player 1 move.
            player1.makeMove(move,board)
            #Check if Player 1 has won.
            if board.isWon(player1.symbol):
                #Print board.
                board.printBoard()
                print('Hooray! Player 1 has won the game!')
                gameIsPlaying = False
            else: #Game is a tie.
                if board.fullBoard():
                    board.printBoard()
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player 2'

        else:
            # Player 2's turn.
            board.printBoard()
            #Player inputs his/her move.
            move = player2.getPlayerMove(board)
            #Make Player 2 move.
            player2.makeMove(move, board)
            #Check if Player 2 has won.
            if board.isWon(player2.symbol):
                #Print board.
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
     #Clear the board if the game is over.
    board = Board()
    #Check if players want to play again.
    if not playAgain():
        break
