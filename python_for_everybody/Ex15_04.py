# Write a program that will read roster data in JSON format, parse the file, and then produce a SQLite
# database that contains a User, Course, and Member table and populate the tables from the data file.

import json
import sqlite3

# Create universitydb in SQLite
conn = sqlite3.connect('universitydb.sqlite')
cur = conn.cursor()

# Drop tables to recreate each time program is run & create tables
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Member;

CREATE TABLE User (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Course (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE
);

CREATE TABLE Member (
      id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
      user_ID INTEGER,
      course_ID INTEGER,
      role INTEGER
);
''')

# Prompt user to enter file name
fname = input('Enter file name:' )
if len(fname) < 1: fname = 'roster_data.json'

# Open json file and parse
data = open(fname).read()
js = json.loads(data)
print('Count of items:', len(data))

# check what json data looks like
# user, class, role
# ['Neiv', 'si430', 0]
# 'Qi', 'si430', 0]
# ['Believe', 'si430', 0]
#for item in js:
#    print(item)

for item in js:

    name = item[0]
    title = item[1]
    role = item[2]

    # Check data
    #print(name, title, role)

    if name is None or title is None or role is None: 
        continue

    cur.execute('INSERT OR IGNORE INTO User (name) VALUES (?)', (name,))
    cur.execute('SELECT id FROM User WHERE name = ?', (name,))
    user_id = cur.fetchone()[0] 

    cur.execute('INSERT OR IGNORE INTO Course (title) VALUES (?)', (title,))
    cur.execute('SELECT id FROM Course WHERE title = ?', (title,))
    course_id = cur.fetchone()[0] 

    cur.execute('''INSERT OR REPLACE INTO Member (user_ID, course_ID, role) 
        VALUES (?, ?, ?)''', (user_id, course_id, role))
    
    conn.commit()