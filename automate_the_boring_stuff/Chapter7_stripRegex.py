#! Python 3
# rewrite the strip() function using Regex - should remove whitespace from
# beginning and end of a string and strip any strings that are passed as args

import re

print('Type in the phrase you would like to modify and remove white space from:')
phrase = input()
# phrase = '    hello   '

print('''Type in the characters you would like to remove from your phrase (not case sensitive):''')
strip = input()
#strip = 'LL'

print('\n \nThe phrase you would like to modify and remove white space from is: \n'
+ phrase + '\n\n' + 'The characters you would like to remove from your phrase are: \n' + strip + '\n')

# Remove any white space characters from an inputted phrase
def trimPhrase(phrase):
    trimRegex = re.compile(r'\S+')
    mo1 = trimRegex.search(phrase)
    trim_phrase = mo1.group()
    #print(len(mo.group()))
    #print(len(phrase))
    return(trim_phrase)

def stripPhrase(trim_phrase):
    stripRegex = re.compile(re.escape(strip), re.IGNORECASE)
    strip_phrase = stripRegex.sub('', trim_phrase)
    print(strip_phrase)
    print(len(strip_phrase))

#enterPhrase()
stripPhrase(trimPhrase(phrase))