'''
Python Script for two players to play Tic_Tac_Toe
'''

from IPython.display import clear_output
import random

#Define global variables
board = [' ']*10

#Define a function to display board to players
def display_board(board):
	clear_output()
	print(' '+board[7]+' | '+board[8]+' | '+board[9])
	print('-----------')
	print(' '+board[4]+' | '+board[5]+' | '+board[6])
	print('-----------')
	print(' '+board[1]+' | '+board[2]+' | '+board[3])

#Define a function to assign marker to players
def player_marker():
	A_Marker = ''
	while A_Marker != 'X' and A_Marker != 'O':
		A_Marker = raw_input("Player A: Do you want to play X or O?").upper()
	if A_Marker == 'X':
		return ('X', 'O')
	else:
		return ('O', 'X')

#Define a function to decide who goes first
def choose_first():
	if random.randint(0,1) == 0:
		return 'Player_A'
	else:
		return 'Player_B'

#Define a function to check whether the position has been taken
def space_check(board, position):
	if board[position] == ' ':
		return True
	else:
		return False

#Ask player to choose a position
def player_choice(board):
	position = 0
	while int(position) not in [1,2,3,4,5,6,7,8,9] or not space_check(board, int(position)):
		position = input('What position do you want to take (1-9)?')
	return int(position)

#Put a marker on the chosen position
def place_marker(board, marker, position):
	board[position]=marker

#Define a function to check if a player wins
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

#Define a function to check if the board is full
def full_board_check(board):
	if ' ' in board[1:]:
		return False
	else:
		return True

#Define a function to ask whether to play again
def replay():
	answer = ''
	while answer not in ['Y', 'N']:
		answer = raw_input('Do you want to play again? Y/N').upper()
	if answer == 'Y':
		return True
	else:
		return False

#Print bbelow message to start game
print('Welcome to Tic Tac Toe!')

while True:
	#Assign marker to both players
	A_Marker, B_Marker = player_marker()
	print('----------------------')
	print('Player A Marker: {}').format(A_Marker)
	print('Player B Marker: {}').format(B_Marker)
	print('----------------------')
	display_board(board)
	#Decide which player goes first
	turn = choose_first()
	print('{} goes first'.format(turn))
	game_on = True

	while game_on:
		if turn == 'Player_A':
			marker = A_Marker
		else:
			marker = B_Marker
		position = player_choice(board)
		place_marker(board, marker, position)
		print('{} takes {}'.format(turn, position))
		display_board(board)

		if win_check(board, marker):
			print('{} wins!'.format(turn))
			break
		elif full_board_check(board):
			print('It is a tie!')
			break
		else:
			print('No wins and no ties. Let move on. ')
			if turn == 'Player_A':
				turn = 'Player_B'
			else:
				turn = 'Player_A'

	if not replay():
		break
