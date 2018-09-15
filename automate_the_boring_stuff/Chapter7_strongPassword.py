#! python3
# detect if a password is strong (must contain a number and a capital letter) and has 8 chars

import re

# check for capital letters, lowercase letters and a number
passRegex = re.compile(r'\w*[A-Z]+\w*\d*')

print('Type in your new password:')
new_pass = input()
#mo = passRegex.search(new_pass)

#check if the password is at least 8 chars
if len(new_pass) < 8:
    print('Passwords must be at least 8 characters. Please enter in a new password.')
# if Regex does not match, prompt user to try again
elif passRegex.search(new_pass) == None:
    print('Password must contain a number and capital letter. Please enter a new password')
else:    
    #print(mo.group())
    print('Strong password! Password accepted')