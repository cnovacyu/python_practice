#! Python 3
# rewrite the strip() function using Regex - should remove whitespace from
# beginning and end of a string and strip any chars that are passed as args

import re

# Ask user to enter phrase to modify and characters to remove from phrase
def definePhrase():
    print('Type in the phrase you would like to modify and remove white space from:')
    # Must set phrase as a global variable to be passed and used in all defs
    global phrase 
    phrase = input()

    print('''Type in the characters you would like to remove from your phrase (not case sensitive):''')
    # Must set phrase as a global variable to be passed and used in all defs
    global strip 
    strip = input()

    print('\n \nThe phrase you would like to modify and remove white space from is: \n'
    + phrase + '\n\n' + 'The characters you would like to remove from your phrase are: \n' + strip + '\n')

# Remove any white space characters from an inputted phrase
def trimPhrase(phrase):
    #Regex searches for any non-white space characters
    #***Need to fix regex - will remove words after a space in a sentence.
    #Want to remove extra spaces before or after words.***
    trimRegex = re.compile(r'(\S)+\s.*\w.*\S.*')
    mo = trimRegex.search(phrase)
    trim_phrase = mo.group()
    #test Regex
    #print(len(phrase))
    #print(len(mo.group()))
    #print(trim_phrase)
    return(trim_phrase)

# Remove any characters the user inputs from the trimmed phrase in trimPhrase
def stripPhrase(trim_phrase, strip):
    #the Regex takes whatever the user inputs and will search the phrase. 
    #will ignore case with re.IGNORECASE
    for char in strip:
        stripRegex = re.compile(char, re.IGNORECASE)
        #the sub function will take the matched Regex and replace it with ''
        strip_phrase = stripRegex.sub('', trim_phrase)
        trim_phrase = strip_phrase
    
    print('Here is your modified phrase: \n' + strip_phrase)
    #test second part of Regex
    #print(len(strip_phrase))

definePhrase()
stripPhrase(trimPhrase(phrase), strip)