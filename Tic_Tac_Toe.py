#Python script for two players playing Tic_Tac_Toe

from __future__ import print_function
from IPython.display import clear_output
import random

#Define a function to display board to players
def display_board(board):
    #clear previous output
    clear_output()
    print(' '+board[7]+' | '+board[8]+' | '+board[9])
    print('-----------')
    print(' '+board[4]+' | '+board[5]+' | '+board[6])
    print('-----------')
    print(' '+board[1]+' | '+board[2]+' | '+board[3])

#Define a function to assign marker to players
def palyer_marker():
    A_Marker = ''
    while A_Marker != 'X' and A_Marker != 'O':
        A_marker = input('Player A: Do you want to play X or O?').upper()
    if A_Marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

#Define a function to decide who goes first
def choose_first():
    if random.randint(0,1) == 0:
        return 'Player A'
    else:
        return 'Player B'

#Define a function to check if player wins
def win_check(board, marker):
    if board[7] == marker and board[8] == marker and board[9] == marker:
        return True
    elif board[4] == marker and board[5] == marker and board[6] == marker:
        return True
    elif board[1] == marker and board[2] == marker and board[3] == marker:
        return True
    elif board[7] == marker and board[4] == marker and board[1] == marker:
        return True
    elif board[8] == marker and board[5] == marker and board[2] == marker:
        return True
    elif board[9] == marker and board[6] == marker and board[3] == marker:
        return True
    elif board[7] == marker and board[5] == marker and board[3] == marker:
        return True
    elif board[9] == marker and board[5] == marker and board[1] == marker:
        return True
    else:
        return False

#Define a function to check if the space players selects is empty
def space_check(board, position):
    if board[position]==' ':
        return True
    else:
        return False

#Define a function to check if the board is full:
def full_board_check(board):
    if ' ' in board:
        return False
    else:
        return True

#Define a function to ask for a players' move
def player_choice(board):
    position = 0
    while int(position) not in [1,2,3,4,5,6,7,8,9] or not space_check(board, int(position)):
        position = input('What position do you want to take (1-9)?')
    return int(position)

#Define a function to assign marker to position
def place_marker(board, marker, position):
    board[position]=marker

#Define a function to ask if player want to play again
def replay():
    answer = ''
    while answer not in ['Y', 'N']:
        answer = input('Do you want to play again? Y/N').upper()
    if answer == 'Y':
        return True
    else:
        return False

#Use above functions to start the game
print('Welcome to Tic Tac Toe!')

while True:
    # Set the game up here
    board = [' ']*10
    playerA_marker, playerB_marker = palyer_marker()
    turn = choose_first()
    print(turn + ' will go first.')
    game_on = True

    while game_on:
        if turn == 'Player A':
            display_board(board)
        #Player A Turn
            position = player_choice(board)
            place_marker(board, player1_marker, position)
    
            if win_check(board, playerA_marker):
                display_board(board)
                print('Player A wins!')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('No one wins!')
                    break
                else:
                    turn = 'Player B'
        # PlayerB's turn.
        else:
            display_board(board)
            position = player_choice(board)
            place_marker(board, playerB_marker, position)
            
            if win_check(board, playerB_marker):
                display_board(board)
                print('Player B wins!')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('No one wins!')
                    break
                else:
                    turn = 'Player A'

    if not replay():
        break