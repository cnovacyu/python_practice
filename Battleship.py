from random import randint

board = []

#Create the board
for x in range(0, 5):
  board.append(["O"] * 5)

#Print the board out with "" from the list. Can combine
#with creating the board above
def print_board(board):
  for row in board:
    print " ".join(row)

print_board(board)

#Choose random numbers. Can probably combine with setting variables below
def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

#Combine in function above
ship_row = random_row(board)
ship_col = random_col(board)

#For debugging only
#print ship_row
#print ship_col

#4 turns allowed to guess. Asks for user input each turn
for turn in range(4):
  print "Turn", turn + 1
  guess_row = int(raw_input("Guess Row: "))
  guess_col = int(raw_input("Guess Col: "))
	
  #Winning condition
  if guess_row == ship_row and guess_col == ship_col:
    print "Congratulations! You sank my battleship!"
    break
  else:
    #Check if guesses are in range of the board. Should change
    #hardcoded range to length of board
    if guess_row not in range(5) or \
      guess_col not in range(5):
      print "Oops, that's not even in the ocean."
    #Check if previously guessed same answer. Should not count turn if
    #guessed previously
    elif board[guess_row][guess_col] == "X":
      print( "You guessed that one already." )
    else:
      #Missed guess. Add an X to the board
      print "You missed my battleship!"
      board[guess_row][guess_col] = "X"
    print_board(board)
    if turn == 3:
      print "Game Over"
      #print "Ship was here:" {:d}{:d}".format(ship_row, ship_col)
      #print where ship was


# You can also add on to your Battleship! program to make it more complex and fun to play. Here are some ideas for enhancements�maybe you can think of some more!

# 1) Make multiple battleships: you'll need to be careful because you need to make sure that you don�t place battleships on top of each other on the game board. You'll also want to make sure that you balance the size of the board with the number of ships so the game is still challenging and fun to play.

# 2) Make battleships of different sizes: this is trickier than it sounds. All the parts of the battleship need to be vertically or horizontally touching and you�ll need to make sure you don�t accidentally place part of a ship off the side of the board.

# 3) Make your game a two-player game.

# Use functions to allow your game to have more features like rematches, statistics and more!
