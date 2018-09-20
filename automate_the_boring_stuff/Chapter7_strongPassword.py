#! python3
# detect if a password is strong (must contain a number, lowercase, and capital letter) and has 8 chars

import re, sys

# check for capital letters, lowercase letters and a number
passRegex = re.compile(r'''(
    ^                   #start anchor
    (?=.*[A-Z])         #positive look ahead assertion to ensure it contains capital letter
    (?=.*[a-z]+)        #positive look ahead assertion to ensure it contains a lowercase letter
    (?=.*\d+)           #positive look ahead assertion to ensure it contains a number
    .{8,}               #ensure string has length of at least 8
    $                   #end anchor
    )''', re.VERBOSE)   #VERBOSE allows regex to be broken into multiple lines

new_pass = ''

def new_password():
    print('Type in your new password:')
    new_pass = input()
    return new_pass
    #mo = passRegex.search(new_pass)

def check_password(new_pass):
    #check if the password is at least 8 chars
    if len(new_pass) < 8:
        print('Passwords must be at least 8 characters. Please enter in a new password.')
    # if Regex does not match, prompt user to try again
    elif passRegex.search(new_pass) == None:
        print('Password must contain a number, lowercase, and capital letter. Please enter a new password')
    else:    
        #print(mo.group())
        print('Strong password! Password accepted')
        return False

while True:
    if check_password(new_password()) == False:
        break