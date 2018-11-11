#! python3
# Walk through a folder tree and search for files that are larger than
# 100 MB and print the filenames and absolute paths.

import os, argparse

# create args for directory and file sizes to search for
parser = argparse.ArgumentParser()
parser.add_argument("src", help="source directory to check for large file sizes")
parser.add_argument("file_size", type=int, help='choose size of file')
parser.add_argument("size_type", choices=['B', 'KB', 'MB', 'GB', 'TB', 'PB'], help='choose file size type')
args = parser.parse_args()

# set args to variables
src = args.src
file_size = args.file_size
size_type = str(args.size_type)

# convert os.path.getsize from bytes into size type specified in arg
convert_dict = {'B':1, 'KB':10, 'MB':20, 'GB':30, 'TB':40, 'PB':50}
factor = convert_dict[size_type]

# walk through a specified directory and check for files larger than file size
# specified. Print filename and absolute path of large files
print()
print('Checking for files that are larger than ' + str(file_size) + ' ' + size_type + ' in: ' + src)

for foldername, subfolders, filenames in os.walk(src):
    for filename in filenames:
        if (os.path.getsize(os.path.join(src, filename)) >> factor) > file_size:
            print(filename + ': ', end='')
            print(os.path.getsize(os.path.join(src, filename)) >> factor, end='')
            print(' ' + size_type)