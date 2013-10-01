#!/usr/local/bin/python2.7
import array


#This function draws a board given the value of each cell
def print_board(board):
	print "Here is the current board:\n"
	print ("     " + board[1] + ' | ' + board[2] + ' | ' + board[3])
	print "     ---------"
	print ("     " + board[4] + ' | ' + board[5] + ' | ' + board[6])
	print "     ---------"
	print ("     " + board[7] + ' | ' + board[8] + ' | ' + board[9])

#This function checks each row, col, diagonal on the board
def check_board(board):
	#check each row
	if (board[1] == board[2] == board[3]):
		return board[1]
	elif (board[4] == board[5] == board[6]):
		return board[4]
	elif (board[7] == board[8] == board[9]):
		return board[7]
	else:
		return ' '
	#check each col
	if (board[1] == board[4] == board[7]):
		return board[1]
	elif (board[2] == board[5] == board[8]):
		return board[2]
	elif (board[3] == board[6] == board[9]):
		return board[3]
	else:
		return ' '
	
	#check each diag
	if (board[1] == board[5] == board[9]):
		return board[1]
	elif (board[7] == board[5] == board[3]):
		return board[7]
	else:
		return ' '
	


#Main

print "\nWelcome to Tic Tac Toe\n"

board = [' '] * 10

board[1] = 'x'
board[2] = 'o'
board[3] = 'x'

#Create graphical board for user
print_board(board)

#TODO handle moves by user and computer

#Check all combinations for a win
done = check_board(board)

#Handle if there is a winner
if done == ' ':
	print "There is no winner yet."
else:
	print "Yay! " + done + " has won the game."
print "\n"
