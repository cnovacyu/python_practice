#! python3
# Walk through a folder tree and search for files with specific file
# extensions. Copy the files to a new folder.

import shutil, os, argparse

parser = argparse.ArgumentParser(description="copy specified type of files to new folder")
parser.add_argument("file_type", help="file extension type")
parser.add_argument("src", help="source directory to copy files from")
parser.add_argument("des", help="destination directory to save copied files")
args = parser.parse_args()

file_type = args.file_type
src = args.src
des = args.des

# Change working directory to location containing text files to search
#os.chdir(r'C:\Users\cnovacy\Documents\01 - Projects\python_practice\automate_the_boring_stuff\Test_Files\cats')

for foldername, subfolders, filenames in os.walk(src):
    for filename in filenames:
        if filename.endswith(file_type):
            start = foldername + '\\'+ filename
            shutil.copy(start, des)