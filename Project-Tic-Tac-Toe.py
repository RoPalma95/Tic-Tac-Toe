board = [['' for i in range(3)] for j in range(3)]
count = 1

for i in range(3):
	for j in range(3):
		board[i][j] = count
		count += 1

board[1][1] = 'X'	
usedSpaces = ()
move = 0

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
	global move

	move = int(input("Enter your move: "))
	
	while(move > 9 or move < 1):
		move = int(input("Invalid input. Try again: "))

	for i in range(3):
		for j in range(3):
			if move == board[i][j]:
				board[i][j] = 'O'
				break
			elif board[i][j] == 'X' or board[i][j] == 'O':
				print("space is not available")
		break

def MakeListOfFreeFields(board):
#
# the function browses the board and builds a list of all the free squares; 
# the list consists of tuples, while each tuple is a pair of row and column numbers
#
	global usedSpaces
	
	for i in range(3):
		for j in range(3):
			if board[i][j] == 'O' or board[i][j] == 'X':
				if (i,j) not in usedSpaces:
					usedSpaces += ((i, j),)

	print(usedSpaces)

def VictoryFor(board, sign):
#
# the function analyzes the board status in order to check if 
# the player using 'O's or 'X's has won the game
#



# def DrawMove(board):
#
# the function draws the computer's move and updates the board
#

DisplayBoard(board)
EnterMove(board)
MakeListOfFreeFields(board)
DisplayBoard(board)
EnterMove(board)
MakeListOfFreeFields(board)
DisplayBoard(board)
