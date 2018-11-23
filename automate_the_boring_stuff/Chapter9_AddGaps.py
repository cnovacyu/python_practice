#! python3
# Insert gaps into numbered files so that a new file can be added

import os, argparse, shutil

# create args for selecting folder to create gaps in numbering
parser = argparse.ArgumentParser()
parser.add_argument('src', help='folder to check numbering of files')
parser.add_argument('starts_with', help='file names to check start with:')
parser.add_argument('file_type', help='specify file type to check')
parser.add_argument('gap', type=int, help='indicate where to create gap in numbered files')
args = parser.parse_args()

# set args to variables
src = args.src
starts_with = args.starts_with
file_type = args.file_type
gap = args.gap

# change directory to folder arg and count number of files in directory
os.chdir(src)
file_count = len(os.listdir(src))

# set gap filename based on gap entered.
gap_file = starts_with + str(gap-1).zfill(3) + file_type

# loop backwards through filenames in directory from arg. Compare filename
# in directory to gap file: if same, break, if not, rename filename 
# to filename + 1 until filename = gap file.
for filename in reversed(os.listdir(src)):  
    if filename == gap_file:
        break
    stdfilename = starts_with + str(file_count+1).zfill(3) + file_type
    shutil.move(filename, stdfilename)
    file_count -= 1