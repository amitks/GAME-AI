# a TIC-TAC-TOE game, implementation of min-max algorithm.

from sys import maxsize as MAXIMUM

board = [None for i in range(9)]

winning_combos = (
	[0, 1, 2], [3, 4, 5], [6, 7, 8],
	[0, 3, 6], [1, 4, 7], [2, 5, 8],
	[0, 4, 8], [2, 4, 6])

def show(board):
	for element in [board[i:i + 3] for i in range(0, len(board), 3)]:
		print element

def available_moves(board):
        return [k for k, v in enumerate(board) if v is None]

def complete(board):
	"""is the game over?"""
	if None not in [v for v in board]:
		return True
	if winner(board) != None:
		return True
	return False

def make_move(board, pos, player):
	board[pos] = player

def get_enemy(player):
	if player == 'X':
		return 'O'
	return 'X'

def winner(board):
	for player in ('X', 'O'):
		positions = get_squares(board, player)
		for combo in winning_combos:
			win = True
			for pos in combo:
				if pos not in positions:
					win = False
			if win:
				return player
        return None

def X_won(board):
	return winner(board) == 'X'

def O_won(board):
	return winner(board) == 'O'

def tied(board):
	return complete(board) == True and winner(board) is None

def get_squares(board, player):
	"""squares that belong to a player"""
	return [k for k, v in enumerate(board) if v == player]

def minmax(board, player):
	print "player=", player
	if complete(board):
		print "board complete"
		if X_won(board):
			return (1, None)
		elif O_won(board):
			return (-1, None)
		elif tied(board):
			return (0, None)

	if player is 'X':
		best = (-2, None)
		for move in available_moves(board):
			if board[move] is None:
				make_move(board, move, player)
				val = minmax(board, get_enemy(player))[0]
				make_move(board, move, None)
				if val > best[0]:
					best = (val, move)
		return best
	else:
		best = (+2, None)
		boardcopy = board[:]
		for move in available_moves(board):
			if board[move] is None:
				make_move(board, move, player)
				val = minmax(board, get_enemy(player))[0]
				make_move(board, move, None)
				if val < best[0]:
					best = (val, move)
		return best

if __name__ == '__main__':

	print "TIC-TAC-TOE: CURRENT TABLE"
	show(board)
	while not complete(board):
		player = 'X'
		player_move = int(raw_input("Next Move: ")) - 1
		if not player_move in available_moves(board):
			continue
		make_move(board, player_move, player)
		show(board)

		if complete(board):
			break

		player = get_enemy(player)
		boardcopy = board[:]
		computer_move = minmax(board, player)[1]
		print "computer_move=", computer_move
		#computer_move = int(raw_input("Next Move: ")) - 1
		make_move(board, computer_move, player)
		show(board)
	
	print "winner is", winner(board)

