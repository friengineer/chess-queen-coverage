from copy import deepcopy

def queen_problem_info():
    print "The Queen Problem (", BOARD_M, "x", BOARD_N, "board)"
    
# Representation of a state
# (number of queens on the board, current state of the board)
#
# 0 represents a square that is not covered by a queen
# 1 represents a square that a queen is on
# 2 represents a square that is covered by a queen
# So on a 4x4 board after placing one queen the state might look like this:
# 
# (1, [[1,2,2,2],
#      [2,2,0,0],
#      [2,0,2,0],
#      [2,0,0,2]])
    
# Returns a matrix of zeros of size mxn to represent the initial state of the board
def queen_get_initial_state(M, N):
	return 0, [ [0 for m in range(N)] for n in range(M)]
	
# Returns the number of squares covered by a queen placed at the coordinate specified by 'action'
def calculate_covered_squares(action, state):
	count = 0
	board = deepcopy(state)
	
	if board[action[0]][action[1]] == 0:
		count += 1
	
	board[action[0]][action[1]] = 1
	
	counter = max(BOARD_M, BOARD_N)
	
	# Checks if the new coordinates are on the board and if so marks them as being covered by the queen
	for i in range(0, counter):
		newm = action[0] - i
		newn = action[1] - i
		
		if newm in range(BOARD_M) and newn in range(BOARD_N):
			if board[newm][newn] == 0:
				board[newm][newn] = 2
				count += 1
			
		newm = action[0] - i
		newn = action[1]
		
		if newm in range(BOARD_M) and newn in range(BOARD_N):
			if board[newm][newn] == 0:
				board[newm][newn] = 2
				count += 1
		
		newm = action[0] - i
		newn = action[1] + i
		
		if newm in range(BOARD_M) and newn in range(BOARD_N):
			if board[newm][newn] == 0:
				board[newm][newn] = 2
				count += 1
		
		newm = action[0]
		newn = action[1] - i
		
		if newm in range(BOARD_M) and newn in range(BOARD_N):
			if board[newm][newn] == 0:
				board[newm][newn] = 2
				count += 1
		
		newm = action[0]
		newn = action[1] + i
		
		if newm in range(BOARD_M) and newn in range(BOARD_N):
			if board[newm][newn] == 0:
				board[newm][newn] = 2
				count += 1
		
		newm = action[0] + i
		newn = action[1] - i
		
		if newm in range(BOARD_M) and newn in range(BOARD_N):
			if board[newm][newn] == 0:
				board[newm][newn] = 2
				count += 1
		
		newm = action[0] + i
		newn = action[1]
		
		if newm in range(BOARD_M) and newn in range(BOARD_N):
			if board[newm][newn] == 0:
				board[newm][newn] = 2
				count += 1
		
		newm = action[0] + i
		newn = action[1] + i
		
		if newm in range(BOARD_M) and newn in range(BOARD_N):
			if board[newm][newn] == 0:
				board[newm][newn] = 2
				count += 1
	
	return count

# Returns a list of coordinates where placing a queen will cover the most amount of squares
def queen_possible_actions(state):
	actions = []
	mostCovered = 0
	
	for m in range(BOARD_M):
		for n in range(BOARD_N):
			coveredSquares = calculate_covered_squares([m, n], state[1])
			
			if coveredSquares > mostCovered:
				if len(actions) > 0:
					del actions[-1]
					
				mostCovered = coveredSquares
				actions.append([m, n])
			elif coveredSquares == mostCovered:
				actions.append([m, n])
	
	return actions

# Places a queen on the board at the coordinate specified by 'action' and marks all squares that are covered by that queen
def queen_successor_state(action, state):
	board = deepcopy(state[1])
		
	board[action[0]][action[1]] = 1
	
	counter = max(BOARD_M, BOARD_N)
	
	# Checks if the new coordinates are on the board and if so marks them as being covered by the queen
	for i in range(0, counter):
		newm = action[0] - i
		newn = action[1] - i
		
		if newm in range(BOARD_M) and newn in range(BOARD_N):
			if board[newm][newn] == 0:
				board[newm][newn] = 2
			
		newm = action[0] - i
		newn = action[1]
		
		if newm in range(BOARD_M) and newn in range(BOARD_N):
			if board[newm][newn] == 0:
				board[newm][newn] = 2
		
		newm = action[0] - i
		newn = action[1] + i
		
		if newm in range(BOARD_M) and newn in range(BOARD_N):
			if board[newm][newn] == 0:
				board[newm][newn] = 2
		
		newm = action[0]
		newn = action[1] - i
		
		if newm in range(BOARD_M) and newn in range(BOARD_N):
			if board[newm][newn] == 0:
				board[newm][newn] = 2
		
		newm = action[0]
		newn = action[1] + i
		
		if newm in range(BOARD_M) and newn in range(BOARD_N):
			if board[newm][newn] == 0:
				board[newm][newn] = 2
		
		newm = action[0] + i
		newn = action[1] - i
		
		if newm in range(BOARD_M) and newn in range(BOARD_N):
			if board[newm][newn] == 0:
				board[newm][newn] = 2
		
		newm = action[0] + i
		newn = action[1]
		
		if newm in range(BOARD_M) and newn in range(BOARD_N):
			if board[newm][newn] == 0:
				board[newm][newn] = 2
		
		newm = action[0] + i
		newn = action[1] + i
		
		if newm in range(BOARD_M) and newn in range(BOARD_N):
			if board[newm][newn] == 0:
				board[newm][newn] = 2
	
	queenNum = state[0] + 1
		
	return queenNum, board
	
# Prints the state of every square of the board
def print_board_state(state):
      board = state[1]
      
      for row in board:
           for square in row:
               print " %2i" % square,
           print

# Tests if all squares are covered by a queen and prints the solution if so
def queen_goal_state(state):
	for m in range(BOARD_M):
		for n in range(BOARD_N):
			if state[1][m][n] == 0:
				return False
				
	print "\nGOAL STATE (1 is a square with a queen on it, 2 is a square that is covered by a queen:\n"
	print_board_state(state)
	print "\nNumber of queens:", state[0]
	
	return True

# Problem specification
def make_qc_problem(m, n):
    global BOARD_M, BOARD_N
    BOARD_M = m
    BOARD_N = n
    
    return ( None,
			 queen_problem_info,
			 queen_get_initial_state(m, n),
			 queen_possible_actions,
			 queen_successor_state,
			 queen_goal_state
			 )
