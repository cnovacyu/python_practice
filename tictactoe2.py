#Prints out the dashes based on the width entered
#Number of dash clusters = width
def horizontal(width):
  print(" ---" * width)
    
#Prints out the |'s based on the width entered
#Number of | = width + 1 to close out the border
def vertical(width):
  print("|   " * (width + 1))

def create_board_game(height, width):
  #Determines how many rows to print out depending on height user entered
  for x in range(height):
    #Calls each of the horizontal and vertical functions to determine what to print on each row
    horizontal(width)
    vertical(width)

  #Close up the board game
  horizontal(width)

#Error handling
#Need further modification here. If 1st condition passes, but 2nd fails,
#it should only re-ask for 2nd condition.
while True:
  try:
    height = int(input("What is the height of your board game? "))
    width = int(input("What is the width of your board game? "))
  except ValueError:
    print("Please enter a valid number")
  else:
    create_board_game(height, width)
    break
