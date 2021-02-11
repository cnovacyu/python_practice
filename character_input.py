# Ask a user to enter their name and age. Print out a message that tells them
# the year they will turn 100 years old

from datetime import datetime

def aging():
    name = input("What is your name? ")
    age = int(input("How old are you? "))

    now = datetime.now()

    old = now.year + (100 - age)

    print(f'{name}, you will be 100 years old in {old}')

aging()