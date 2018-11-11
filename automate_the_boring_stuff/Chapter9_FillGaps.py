#! python3
# Find all files with a given prefix such as spam001.txt, spam002.txt, etc
# in a single folder and locate any gaps in the numbering. Rename all later
# files to close the numbering gap.

import os, argparse, shutil

# create args for selecting folder to check numbering of files
parser = argparse.ArgumentParser()
parser.add_argument('src', help='folder to check numbering of files')
parser.add_argument('starts_with', help='file names to check start with:')
parser.add_argument('file_type', help='specify file type to check')
args = parser.parse_args()

# set args to variables
src = args.src
starts_with = args.starts_with
file_type = args.file_type

# change directory to folder arg
os.chdir(src)

# check for gaps in filename numbering. If any gaps, rename file to fill in gap
num = 1
for filename in os.listdir(src):
    stdfilename = starts_with + str(num).zfill(3) + file_type
    if not os.path.exists(stdfilename):
        shutil.move(filename, stdfilename)
    num += 1