#! python3
# Walk through a folder tree and search for files with specific file
# extensions. Copy the files to a new folder.

import shutil, os

# Change working directory to location containing text files to search
os.chdir(r'C:\Users\cnovacy\Documents\01 - Projects\python_practice\automate_the_boring_stuff\Test_Files\cats')

for foldername, subfolders, filenames in os.walk(r'C:\Users\cnovacy\Documents\01 - Projects\python_practice\automate_the_boring_stuff\Test_Files\cats'):
    for filename in filenames:
        if filename.endswith('.txt'):
            src = foldername + '\\'+ filename
            shutil.copy(src, r'C:\Users\cnovacy\Documents\01 - Projects\python_practice\automate_the_boring_stuff\Test_Files\cats_new')