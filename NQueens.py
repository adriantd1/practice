global n, queens, done
n = int(input())
board = [['.' for x in range(n)] for y in range(n)]
queens = n
done = False

def isSafe(x,y):
	safe = True
	for i in board[x]:
		if i == 'Q':
			return False
	for i in range(n):
		if board[i][y] == 'Q':
			return False
	tempx = x+1
	tempy = y+1
	while tempx<n and tempy<n:
		if board[tempx][tempy] == 'Q':
			return False
		tempx += 1
		tempy += 1
	tempx = x-1
	tempy = y+1
	while tempx>=0 and tempy<n:
		if board[tempx][tempy] == 'Q':
			return False
		tempx -= 1
		tempy += 1
	tempx = x+1
	tempy = y-1
	while tempx<n and tempy>=0:
		if board[tempx][tempy] == 'Q':
			return False
		tempx += 1
		tempy -= 1
	tempx = x-1
	tempy = y-1
	while tempx>=0 and tempy>=0:
		if board[tempx][tempy] == 'Q':
			return False
		tempx -= 1
		tempy -= 1
	return safe
		
def placeQueens(x,y):
	global queens, n, done
	if y==n:
		placeQueens(x+1,0)
	elif x == n:
		if queens == 0:
			for i in board:
				print(i)
			done = True
			return
	else:
		if done:
			return
		if queens > 0 and isSafe(x,y):
			queens -= 1
			board[x][y] = 'Q'
			
			placeQueens(x, y+1)
			
			board[x][y] = '.'
			queens += 1
		
		placeQueens(x, y+1)
		
placeQueens(0,0)
