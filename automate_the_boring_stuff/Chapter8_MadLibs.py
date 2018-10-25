import os, re, pyperclip

# Open the file and read the contents
madLibFile = open(r'C:\Users\cnovacy\Documents\01 - Projects\python_practice\automate_the_boring_stuff\Test_Files\MadLibs.txt')
madLibContent = madLibFile.read()
madLibFile.close()
print(madLibContent)

# Create Regex to search for variables and replace with user input
# loop through each variable in the mad lib
variables = ['adjective', 'noun', 'verb', 'noun']
for var in variables:
    print("Enter a " + var + ':')
    libInput = input()
    madLibRegex = re.compile((var)+'?', re.IGNORECASE)
    #the sub function will take the matched Regex and replace it with user input
    #sub functions has count parameter to indicate how many subs should occur
    madLibFiller = madLibRegex.sub(libInput, madLibContent, 1)
    madLibContent = madLibFiller

print(madLibContent)

#Copy the completed mad lib and write to a new file
pyperclip.copy(madLibContent)
madLibResponseFile = open(r'C:\Users\cnovacy\Documents\01 - Projects\python_practice\automate_the_boring_stuff\Test_Files\madLibResponseFile.txt', 'w')
madLibResponseFile.write(pyperclip.paste())
madLibResponseFile.close()