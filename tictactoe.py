#!/usr/local/bin/python2.7
import array
import string


###########################################################
# UNIT TESTS

#RUn unit tests
def Run_All_Tests():
	Test_FullBoard()
	Test_OneMove()

#Test whether full board is recognized
def Test_FullBoard():
	#Create board
	board = [' ','X','O','X','O','X','O','X','O','X']
	print_board(board)

	#Determine current player
	curplayer = 'X'

	#Find best move
	(cell,score) = best_move(board,curplayer)

	#Make sure board returned is correct
	assert(score == 1)
	assert(cell == 0)

	#Make sure player lost
	curplayer = 'O'
	(cell,score) = best_move(board,curplayer)
	assert(score == -1)
	assert(cell == 0)

	#Create tied board
	board = [' ','X','O','X','O','X','O','O','X','O']
	print_board(board)

	#Make sure both players return tie
	curplayer = 'X'
	(cell,score) = best_move(board,curplayer)
	assert(score == 0)
	assert(cell == 0)
	
	curplayer = 'O'
	(cell,score) = best_move(board,curplayer)
	assert(score == 0)
	assert(cell == 0)


#Test whether one move works
def Test_OneMove():
	#Create board
	board = [' ','X','O','X','O','X','O','O',' ','O']
	print_board(board)
	
	#Determine current player
	curplayer = 'X'
	(cell,score) = best_move(board,curplayer)
	print "the cell is " + str(cell)
	assert(cell == 8)

	#Find best (only) move


	#Make sure board returned is correct

"""
If one move gets filled in
	if winner is recognized
	if loser is recognized
if board is left empty if there is already a winner

"""





###########################################################


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
def comp_move(board,compicon):
	"""	
	#TODO delete next three lines later
	for i in range(1,10):
		if (board[i] == ' '):
			return i
	"""
	#init vars
	optscore = -1
	optcell = 0

	#find most optimal cell and score
	(optcell,optscore) = best_move(board,compicon)

	#return most optimal move
	return optcell


#Recursive function (minimax)
def best_move(board,curplayer):

	cell = 0
	score = -1

	#check for a winner
	winner = check_win(board)
	board_full = full_board(board)

	#there is no winner
	if(winner == ' '):
		if(board_full == 0):
		#there's a tie
			score = 0
		else:
			scoresarray = []
			#try each remaining cell in order
			for i in range(1,10):
				#temporarily fill in empty cells
				if (board[i] == ' '):
					#print i
					board[i] = curplayer
				
					#change player
					if(curplayer == 'O'):
						curplayer = 'X'
					else:
						curplayer = 'O'
				
					print_board(board)
					temp,score = best_move(board,curplayer)
					score = score*(-1)

					#create array of cells and scores
					tup = (i,score)
					scoresarray.append(tup)
					
					#print scoresarray
					#print "AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH"

					#clear temp cell
					board[i] = ' '
					
					#print "current cell checked is " + str(i)

#			print "done checking all cells"
			#find optimal in array (at current depth)
			optscore = -1
			for i in range(0,(len(scoresarray))):
#				print scoresarray
#				print "cell is " + str(i) + ", optcell is " + str(cell) + ", score is " + str(score) + ",optscore is " + str(optscore)
				if (scoresarray[i][1] >= optscore):
					optscore = scoresarray[i][1]
					cell = scoresarray[i][0]	
			return (cell,optscore)

	#the winner is me
	elif(winner == curplayer):
		score = 1
	#the winner is opponent
	else:
		score = -1

	return (cell,score)

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
print ("     " + '7' + ' | ' + '8' + ' | ' + '9\n')


Run_All_Tests()


while True:
	#Let user decide player
	print("Player X goes first.")
	icon = raw_input("Would you like to play as (X) or (O)?: ")
	icon = icon.upper()
	if (icon == 'X' or icon == 'O'):
		#create game board
		board = [' '] * 10

		#Create graphical board for user
		print_board(board)
		break
	else:
		print "Invalid input. Try again\n"

if(icon == 'X'):
	curplayer = 1
	human = 'X'
	comp = 'O'
else:
	curplayer = 2
	human = 'O'
	comp = 'X'

while True:
#Do this until there is a win or tie

	if(curplayer == 1):
	#Handle human move
		
		cell = user_move(board)
		board[cell] = human
		print "\nYou played cell " + str(cell) + ".\n"
		curplayer = 2

	else:
	#Handle computer plays

		cell = comp_move(board,comp)
		board[cell] = comp
		print "\nComputer played cell " + str(cell) + ".\n"
		curplayer = 1

		print_board(board)

		#Check all combinations for a win
		done = check_win(board)

	#Check all combinations for a win
	done = check_win(board)
	#Exit if the game is over
		#means done has a winner, or there are no blank cells
	if (done != ' ' or full_board == 0):
		break
#Show final board
print_board(board)

if (done == human):
	print "Game over! You have won the game."
elif (done == comp):
	print "Game over! The computer has won the game."
else:
	print "Game over! There was a tie."

print "\n"
