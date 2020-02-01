#Write a program that will read an iTunes export file in XML and produce a properly normalized database using SQLite

import xml.etree.ElementTree as ET
import sqlite3

#create database in SQLite
conn = sqlite3.connect('musicdb.sqlite')
cur = conn.cursor()

#drop tables each time program is run and recreate all tables
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

data = input('Enter xml file name: ')
if len(data) < 1:
    data = 'Library.xml'

tree = ET.parse(data)
items = tree.findall('dict/dict/dict')
print('Item count:', len(items))

# Example of xml data from Library.xml file
# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>

# Have to lookup items in the list that we parsed from xml data. The Library.xml data is structured 
# differently than typical xml data would be
def lookup(d, key):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None

# Looking up each item in our list to find each element
for item in items:
    if (lookup(item, 'Track ID') is None) : continue

    name = lookup(item, 'Name')
    artist = lookup(item, 'Artist')
    album = lookup(item, 'Album')
    genre = lookup(item, 'Genre')
    length = lookup(item, 'Total Time')
    rating = lookup(item, 'Rating')
    count = lookup(item, 'Play Count')

    # Prevent program from crashing if there is no value found for each element 
    if name is None or artist is None or genre is None or album is None: 
        continue

    #debug that data from xml was pulled correctly
    #print(name, artist, album, genre, length, rating, count)

    # Insert pulled info from xml data into SQLite musicdb 
    cur.execute('INSERT OR IGNORE INTO Artist (name) VALUES (?)', (artist,))
    cur.execute('SELECT id FROM Artist WHERE name = ?', (artist,))
    artist_id = cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Genre (name) VALUES (?)', (genre,))
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre,))
    genre_id = cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Album (artist_id, title) VALUES (? , ?)', (artist_id, album))
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album,))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track (title, album_id, genre_id, len, rating, count) 
        VALUES (?, ?, ?, ?, ?, ?)''', (name, album_id, genre_id, length, rating, count))

    conn.commit()
    
print('Commit to database complete')