from random import randint

def isCellValid(board,i,j):
	for r in range(9):
		if board[r][j] == board[i][j] and i != r:
			return False

	for c in range(9):
		if board[i][c] == board[i][j] and j != c:
			return False

	row_top_bound,col_left_bound =  0,0

	if i <= 2:
		row_top_bound = 0
	elif i <= 5:
		row_top_bound = 3
	else:
		row_top_bound = 6



	if j <= 2:
		col_left_bound = 0
	elif j <= 5:
		col_left_bound = 3
	else:
		col_left_bound = 6


	for r in range(row_top_bound,row_top_bound+3):
		for c in range(col_left_bound,col_left_bound+3):
			if board[r][c] == board[i][j] and (r,c) != (i,j):
				return False

	return True

def isMatrixValid(board):
	for i in range(9):
		for j in range(9):
			if not isCellValid(board,i,j):
				return False
	return True

def prntBoard(board):

	print('______________________')
	for i in range(9):
		for j in range(9):
			print(board[i][j],end=' ')
			if (j+1) %3 == 0 and j:
				print('| ',end='')
		
		if  (i+1) % 3 == 0:
			print('\n______________________')

		else:
			print('\n',end='')

def findNextEmptyCell(board):
	for r in range(0,9):
		for c in range(0,9):
			if board[r][c] == "*":
				return r,c

	return -1,-1

def solveSudoko(board):

	r,c = findNextEmptyCell(board)
	print('attempting...')
	
	if r == -1:
		if isMatrixValid(board):
			prntBoard(board)
			print("sol above")
			return True

		else:
			return False


	for num in range(1,10):
		board[r][c] = str(num)
		if isCellValid(board,r,c):
			res = solveSudoko(board)
			if res:
				return True
		board[r][c] = "*"


	return False
	

testBoard = [[a for a in "*********"],
			[a for a in "*********"],
			[a for a in "*********"],
			[a for a in "*********"],
			[a for a in "*********"],
			[a for a in "*********"],
			[a for a in "*********"],
			[a for a in "*********"],
			[a for a in "*********"]]

solveSudoko(testBoard)

# print(isMatrixValid(testBoard))
