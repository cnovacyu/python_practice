#! python 3
# Open all .txt files in a folder and search for any line that matches
# user input. Results are printed to the terminal.

import os, re

# Prompt user for a search phrase
print('Enter the phrase you would like to search in text files: ')
search = input()

# Regex set to phrase entered by user
searchRegex = re.compile(search, re.IGNORECASE)

# Change working directory to location containing text files to search
os.chdir(r'C:\Users\cnovacy\Documents\01 - Projects\python_practice\automate_the_boring_stuff\Test_Files')

# Check each file in the directory above for search phrase entered by user
for filename in os.listdir(r'C:\Users\cnovacy\Documents\01 - Projects\python_practice\automate_the_boring_stuff\Test_Files'):
    # Only search text files
    if filename.endswith('.txt'):
        # Troubleshoot to check files
        #print(filename)
        # Open each file and read content
        checkFile = open(filename, 'r')
        fileContent = checkFile.read()
        checkFile.close()
        # Search each file for the Regex phrase entered by the user
        #mo = searchRegex.search(fileContent)
        mo = searchRegex.findall(fileContent)
        print(filename + ' contains your search phrase: \"' + search + '\" ' + str(len(mo)) + ' times')