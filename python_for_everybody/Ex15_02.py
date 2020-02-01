# Write a program that will read the mailbox data (mbox.txt) and count the number of email messages per organization 
# (i.e. domain name of the email address) using a database with the following schema to maintain the counts.

import urllib.request, urllib.error
import sqlite3
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Connect to the Email DB server
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

# Drop Counts table and recreate everything program is run
cur.execute('DROP TABLE IF EXISTS Counts')

#Create table
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

# Enter file name to open and pull data from
fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    orgs = re.findall('.+@(.+)', email)
    #debug
    # print(orgs)
    for org in orgs:
        cur.execute('SELECT count FROM Counts WHERE org = ?', (org,))
        row = cur.fetchone()
        if row is None:
            cur.execute('INSERT INTO Counts (org, count) VALUES (?,1)', (org,))
        else:
            cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))
        
conn.commit()

# #Sort database by largest count and print out first line
cur.execute('SELECT * FROM Counts ORDER BY count DESC LIMIT 1')
row = cur.fetchone()
print(row)

cur.close()