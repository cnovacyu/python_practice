game = [[2, 2, 0],
	[2, 1, 0],
	[1, 1, 1]]

player1 = 1
player2 = 2

def who_wins(game):
  for row in game:
    if row.count(player1) == 3:
      print("Player1 wins!")
    elif row.count(player2) == 3:
      print("Player2 wins!")


def arrange_columns(game):

  game_c = []
  list1 = []
  list2 = []
  list3 = []

  for row in range(0, len(game)):
    list1.append(game[row][0])

  game_c.append(list1)

  for row in range(0, len(game)):
    list2.append(game[row][1])

  game_c.append(list2)

  for row in range(0, len(game)):
    list3.append(game[row][2])

  game_c.append(list3)
  
  who_wins(game_c)


def arrange_diagonals(game):
  
  game_d = []
  list1 = []
  list2 = []

  for row in range(0, len(game)):
    list1.append(game[row][row])

  for row in range(0, len(game)):
    list2.append(game[row][len(game) - 1 - row])

  game_d.append(list1)
  game_d.append(list2)

  who_wins(game_d)


def play_game():
  who_wins(game)
  arrange_columns(game)
  arrange_diagonals(game)

play_game()
