#Write a program to read through the mbox-short.txt and figure out the distribution by hour 
# of the day for each of the messages. You can pull the hour out from the 'From ' line by 
# finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

d = dict()
for line in handle:
    words = line.split()
    if len(words) < 1 or words[0] != 'From':
        continue
    time = words[5]
    times = time.split(":")
    hour = times[0]
    #print(hour)
    d[hour] = d.get(hour, 0) + 1
        
l = list()
for (k,v) in d.items():
    l.append((k,v))

l.sort()

for(k,v) in l:
    print(k, v)