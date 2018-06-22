def game_size():
    size = input("What size of board game would you like? ")
    if size.isalpha() or size == '':
        print ("Please enter a valid size." )
        game_size()
    elif int(size) >= 20:
        print("That's a huge board game!")
        game_size()
    else:
        return size
        
def create_board_game():
    size = int(game_size())
    
    for x in range(size):
        print(" ---" * size)
        print("|   " * (size + 1))
        
    print(" ---" * size)
       
create_board_game()
