import os, re

# Open the file and read the contents
madLibFile = open(r'C:\Users\cnovacy\Documents\01 - Projects\python_practice\automate_the_boring_stuff\Test_Files\MadLibs.txt')
madLibContent = madLibFile.read()
print(madLibContent)


# Create Regex to search for variables
variables = ['adjective', 'noun', 'verb', 'noun']
for var in variables:
    print("Enter a " + var + ':')
    libInput = input()
    madLibRegex = re.compile((var)+'?', re.IGNORECASE)
    #the sub function will take the matched Regex and replace it with user input
    madLibFiller = madLibRegex.sub(libInput, madLibContent)
    madLibContent = madLibFiller

print(madLibFiller)





# Copy the new add lib and save it in a new file