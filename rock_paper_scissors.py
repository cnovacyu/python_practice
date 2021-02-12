# Make a two-player rock-paper-scissors game. Ask for player plays (using input), compare them, print out
# a message of congratulations to the winner, and ask if the players want to start a new game

# Added bomb as a secret option that always wins against rock, paper, and scissors

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