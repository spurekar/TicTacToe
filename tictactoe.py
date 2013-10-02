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

#This function handles the user's move
def user_move():
	while True:
		#ask user for cell
		cell = raw_input("Pick a cell to play (1-9): ")

		#validate cell
		try:
			cell = int(cell)
			if (cell >= 1 and cell <= 9):
				#return cell number
				return cell
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
	

#Main

print "\nWelcome to Tic Tac Toe"
print "Here is the number for each cell"
print ("     " + '1' + ' | ' + '2' + ' | ' + '3')
print "     ---------"
print ("     " + '4' + ' | ' + '5' + ' | ' + '6')
print "     ---------"
print ("     " + '7' + ' | ' + '8' + ' | ' + '9')

board = [' '] * 10
movecount = 0

#Create graphical board for user
print_board(board)

while True:

	#Handle human move
	cell = user_move()
	movecount+= 1
	board[cell] = 'X'

	print_board(board)

	#Handle computer plays
	#cell = comp_move()

	#Check all combinations for a win
	done = check_win(board)


	print board

	#Exit if the game is over
	if (done != ' ' or movecount == 9):
		break


if (done != ' '):
	print "Yay! " + done + " has won the game."
else:
	print "There was a tie."


print "\n"

