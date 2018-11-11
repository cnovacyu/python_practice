#! python3
# Walk through a folder tree and search for files with specific file
# extensions. Copy the files to a new folder.

import shutil, os, argparse

# create args that need to be populated to run script
# args for file extenstion, source directory, and destination directory 
# for copied specified files
parser = argparse.ArgumentParser(description="copy specified type of files to new folder")
parser.add_argument("file_type", help="file extension type")
parser.add_argument("src", help="source directory to copy files from")
parser.add_argument("des", help="destination directory to save copied files")
args = parser.parse_args()

# set args to variables
file_type = args.file_type
src = args.src
des = args.des

# walk through a specified directory and copy file if it is the specified
# file extension into a destination folder specified
for foldername, subfolders, filenames in os.walk(src):
    for filename in filenames:
        if filename.endswith(file_type):
            start = foldername + '\\'+ filename
            shutil.copy(start, des)