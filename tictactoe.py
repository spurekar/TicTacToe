#!/usr/local/bin/python2.7
import array

#This function draws a board given the value of each cell
def print_board(board):
	print "This is the current board:\n"
	print ("     " + board[1] + ' | ' + board[2] + ' | ' + board[3])
	print "     ---------"
	print ("     " + board[4] + ' | ' + board[5] + ' | ' + board[6])
	print "     ---------"
	print ("     " + board[7] + ' | ' + board[8] + ' | ' + board[9])
	print "\n"

#This function handles the user's move
def user_move(board):
	while True:
		#ask user for cell
		cell = raw_input("Pick a cell to play (1-9): ")

		#validate cell
		try:
			cell = int(cell)
			if (cell >= 1 and cell <= 9):
				#return cell number
				if(board[cell] == ' '):
					return cell
				else:
					print "Invalid input"
			else:
				print "Invalid input"
		except ValueError:
			print "Invalid input"
	

#This function checks each row, col, diagonal on the board
def check_win(board):
	#check each row
	if (board[1] == board[2] == board[3] and board[1] != ' '):
		return board[1]
	elif (board[4] == board[5] == board[6] and board[4] != ' '):
		return board[4]
	elif (board[7] == board[8] == board[9] and board[7] != ' '):
		return board[7]
	
	#check each col
	elif (board[1] == board[4] == board[7] and board[1] != ' '):
		return board[1]
	elif (board[2] == board[5] == board[8] and board[2] != ' '):
		return board[2]
	elif (board[3] == board[6] == board[9] and board[3] != ' '):
		return board[3]
	
	#check each diag
	elif (board[1] == board[5] == board[9] and board[1] != ' '):
		return board[1]
	elif (board[7] == board[5] == board[3] and board[7] != ' '):
		return board[7]
	else:
		return ' '

#This function picks the most optimal move for the computer
def comp_move(board):
	
	#init vars
	optscore = -1
	optcell = 0
	nextturn = 'O'

	#find most optimal cell and score
	(optcell,optscore) = poss_move(board,optscore,optcell,nextturn)

	#return most optimal move
	return optcell


#Recursive function (minimax)
def poss_move(board,optscore,optcell,nextturn):
	
	#check if comp won
	if(check_win(board) == 'O'):
		score = 1
	#check if user won
	elif(check_win(board) == 'X'):
		score = -1
	#check if there is a tie
	elif(check_win(board) == ' ' and full_board == 0):
		score = 0
	#check if there is no winner yet
	else:
		#go through each empty cell
		for i in range(1,10):
			if(board[i] != ' '):
				continue
			else:
				#we have an empty cell
				#inhabit empty cell
				board[i] = nextturn
				if (nextturn == 'O'):
					nextturn = 'X'
				else:
					nextturn = 'O'
				#score	
				(cell,score) = poss_move(board,optscore,optcell,nextturn)
				
			#track score
			if (score > optscore):
				optscore = score
				optcell = cell
			#clear same cell
			board[i] = ' '
	
	return (optcell, optscore)


	"""
	#return most optimal cell
	if (depth == 0 or full_board == 0):
		return cell
	if (score < 0)
		poss_move(depth-1,board,score)

	#find first empty cell
	cell = full_board(board)
	if ((depth % 2) == 0):
		board[cell] = 'X'
	else:
		board[cell] = 'O'

	#check if there is a winner
	if(check_win(board) == 'O'):
		score = 1
		poss_move(depth-1,board,score)

	if (depth 

	return cell
	"""

#This function returns an empty cell if possible, otherwise indicates a full board
def full_board(board):
	for i in range(1,10):
		if (board[i] == ' '):
			return i
	return 0

#Main

print "\nWelcome to Tic Tac Toe"
print "Here is the number for each cell"
print ("     " + '1' + ' | ' + '2' + ' | ' + '3')
print "     ---------"
print ("     " + '4' + ' | ' + '5' + ' | ' + '6')
print "     ---------"
print ("     " + '7' + ' | ' + '8' + ' | ' + '9')

board = [' '] * 10

#Create graphical board for user
print_board(board)

while True:

	#Handle human move
	cell = user_move(board)
	board[cell] = 'X'
	print "\nYou played cell " + str(cell) + "."

	#Check all combinations for a win
	done = check_win(board)
	#Exit if the game is over
		#means done has a winner, or there are no blank cells
	if (done != ' ' or full_board == 0):
		break

	#Handle computer plays
	cell = comp_move(board)
	board[cell] = 'O'
	print "Computer played cell " + str(cell) + ".\n"
	
	print_board(board)

	#Check all combinations for a win
	done = check_win(board)

	#TODO delete me later
	#print board

	#Exit if the game is over
		#means done has a winner, or there are no blank cells
	if (done != ' ' or full_board == 0):
		break

#Show final board
print_board(board)

if (done != ' '):
	print "Yay! " + done + " has won the game."
else:
	print "There was a tie."


print "\n"

