# Use the file name mbox-short.txt as the file name
#Count these lines and extract the floating point values from each of the lines and compute the average 
# of those values and produce an output as shown below. Do not use the sum() function or a variable 
# named sum in your solution. You can download the sample data at  http://www.py4e.com/code3/mbox-short.txt
# when you are testing below enter mbox-short.txt as the file name.

#fname = input("Enter file name: ")
#fh = open(fname)

#open up and create handle for the file
fh = open('mbox-short.txt')

count = 0 
spam = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    if line.startswith("X-DSPAM-Confidence"):
        count = count + 1
        #if the line starts with X-DSPAM... then find the position of ':'
        fpos = line.find(":")
        #capture the confidence interval value
        conf = line[fpos+1:]
        #remove any blank spaces, convert to float, and calculate rolling sum
        spam = spam + float(conf.strip())

#Compute average after finishing looping through entire file
print("Average spam confidence:", (spam / count))