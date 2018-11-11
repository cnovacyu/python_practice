#! python3
# Walk through a folder tree and search for files that are larger than
# 100 MB and print the filenames and absolute paths.

import os, argparse

# create arg for directory to search for large files
parser = argparse.ArgumentParser()
parser.add_argument("src", help="source directory to check for large file sizes")
args = parser.parse_args()

# set arg to variables
src = args.src

# walk through a specified directory and check for files larger than 100 MB
# print filename and absolute path of large files
for foldername, subfolders, filenames in os.walk(src):
    for filename in filenames:
        if (os.path.getsize(os.path.join(src, filename)) >> 20) > 100:
            print(filename + ':'),
            print(os.path.getsize(os.path.join(src, filename)) >> 20)
        