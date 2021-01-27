import sys

def winner(plays, wins):

    if plays[1] == plays[2]:
        print("It's a tie!")
    elif plays[2] in wins[plays[1]]:
        print('Player 1 is the winner!\n')
    else:
        print('Player 2 is the winner!\n')

    print('')


def play_again():

    print('Would you like to play again? (Y/N)')

    play_again = input().lower()

    while True:
        if play_again not in ['y', 'n']:
             play_again = input(f'Please choose a valid entry. Would you like to play again? (Y/N)\n').lower()
        elif play_again == 'y':
            rock_paper_scissors()
        else:
            sys.exit()


def rock_paper_scissors():
    
    plays = {}
    wins = {'rock':'scissors', 'scissors':'paper', 'paper':'rock', 'bomb':['rock', 'paper', 'scissors']}

    for i in range(1,3):
        choice= input(f'Player {i}: Rock, Paper, Scissors?\n').lower()

        if choice not in wins.keys():
            choice= input(f'Please choose a valid entry. Player {i}: Rock, Paper, Scissors?\n').lower()
        else:
            plays[i] = choice

    winner(plays, wins)

    play_again()


rock_paper_scissors()