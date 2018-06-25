#Prints out the horizontal lines across based on the width entered
def horizontal(width):
  print(" ---" * width)
    
def vertical(width):
  print("|   " * (width + 1))

def create_board_game(height, width):
  #Will print out vertically depending on height user entered
  for x in range(height):
    #Calls each of the horizontal and vertical functions
    horizontal(width)
    vertical(width)

  #Close up the board game
  horizontal(width)

#Error handling      
while True:
  try:
    height = int(input("What is the height of your board game? "))  
  except ValueError:
    print("Please enter a valid height")
  try:
    width = int(input("What is the width of your board game? "))
  except ValueError:
    print("Please enter a valid width")
  else:
    create_board_game(height, width)
    break
