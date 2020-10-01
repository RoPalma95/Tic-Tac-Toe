from os import terminal_size
from random import randrange

board = [['' for i in range(3)] for j in range(3)]
count = 1

for i in range(3):
	for j in range(3):
		board[i][j] = count
		count += 1

board[1][1] = 'X'	
move = 0
usedSpaces = ((1, 1),)
winner = False

def DisplayBoard(board):
	#
	# the function accepts one parameter containing the board's current status
	# and prints it out to the console
	#
	print('+-------'*3, '+', sep = '')
	print('|       '*3, '|', sep = '')
	print('|   ', board[0][0], '   ', '|   ', board[0][1], '   ','|   ', board[0][2], '   |', sep = '')
	print('|       '*3, '|', sep = '')
	print('+-------'*3, '+', sep = '')
	print('|       '*3, '|', sep = '')
	print('|   ', board[1][0], '   ', '|   ', board[1][1], '   ','|   ', board[1][2], '   |', sep = '')
	print('|       '*3, '|', sep = '')
	print('+-------'*3, '+', sep = '')
	print('|       '*3, '|', sep = '')
	print('|   ', board[2][0], '   ', '|   ', board[2][1], '   ','|   ', board[2][2], '   |', sep = '')
	print('|       '*3, '|', sep = '')
	print('+-------'*3, '+\n', sep = '')

def EnterMove(board):
#
# the function accepts the board current status, asks the user about their move, 
# checks the input and updates the board according to the user's decision
#	
	move = int(input("Enter your move: "))
	
	while move < 1 or move > 9:
		move = int(input("Invalid input. Try again: "))

	for pair in usedSpaces:
		row, column = pair
		for i in range(3):
			for j in range(3):
				if move == board[i][j] and (i != row or j != column):
					board[i][j] = 'O'
	

def MakeListOfUsedFields(board):
#
# the function browses the board and builds a list of all the free squares; 
# the list consists of tuples, while each tuple is a pair of row and column numbers
#
	global usedSpaces

	for i in range(3):
		for j in range(3):
			if board[i][j] == 'O' or board[i][j] == 'X':
				if (i, j) not in usedSpaces:
					usedSpaces += ((i,j),)

def VictoryFor(board, sign):
#
# the function analyzes the board status in order to check if 
# the player using 'O's or 'X's has won the game
#
	winner = ''

# checking if all elements in the row are  the same:

	for i in range(3):
		counter = 0
		for j in range(3):
			if board[i][j] == sign:
				counter += 1
		if counter == 3:
			winner = sign

# checking if all the elements in the column are the same

	for i in range(3):
		counter = 0
		for j in range(3):
			if board[j][i] == sign:
				counter += 1
		if counter == 3:
			winner = sign

	return winner
	


def DrawMove(board):
#
# the function draws the computer's move and updates the board
#
	valid = False

	while valid == False:
		computerMove = randrange(1, 10)
		for pair in usedSpaces:
			row, column = pair
			for i in range(3):
				for j in range(3):
					if computerMove == board[i][j] and (i != row or j != column):
						board[i][j] = 'X'
						valid = True
	
DisplayBoard(board)

for i in range(4):
	EnterMove(board)
	MakeListOfUsedFields(board)
	DisplayBoard(board)
	victor = VictoryFor(board, 'O')
	if victor == 'O':
		print('You won!')
		winner = True
		break
	DrawMove(board)
	MakeListOfUsedFields(board)
	DisplayBoard(board)
	victor = VictoryFor(board, 'X')
	if victor == 'X':
		print('Computer won :(')
		winner = True
		break

if not winner: 
	print("It's a tie.")