# ask the user for a string and print out whether it is a palindrome or not

def string_lists():

    word = input('Please enter a word: ').upper()
    print(f'Your word is {word}')

    new_word = word[::-1]

    print(f'{word} backwards is {new_word}')

    if new_word == word:
        print(f'{word} is a palindrome!')
    else:
        print(f'Try again! {word} is not a palindrome.')
    
string_lists()