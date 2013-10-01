#!/usr/local/bin/python2.7


#Internal board for storage
board = []
for x in range(0,3):
	board.append(["*"]*3)


#Create graphic for user
def print_board(board):
	letter = ["1","2","3"]
	print "   A B C"
	print "--------"
	for i, row in zip(letter, board):
		print (i + "| " + " ".join(row))
	print " "


print " "
print_board(board)
