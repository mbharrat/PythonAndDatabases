#import statements
import xml.etree.ElementTree as ElementTree
import sqlite3

#create db file
conn = sqlite3.connect('mytrack.sqlite')
cur = conn.cursor()

#if table exists drop...if not create it
cur.executescript('''
    DROP TABLE IF EXISTS Artist;
    DROP TABLE IF EXISTS Genre;
    DROP TABLE IF EXISTS Album;
    DROP TABLE IF EXISTS Track;

    CREATE TABLE Artist (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE
    );

    CREATE TABLE Genre (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE
    );

    CREATE TABLE Album (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        artist_id INTEGER,
        title TEXT UNIQUE
    );

    CREATE TABLE Track (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT UNIQUE,
        album_id INTEGER,
        genre_id INTEGER,
        len INTEGER,
        rating INTEGER,
        count INTEGER
    );
    ''')
#prompt for file imput
fname = raw_input('Enter the file name: ')
if (len(fname) < 1) : fname = 'Library.xml'
#-------------------------------------------------------
#EXAMPLE XML
# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>
#-------------------------------------------------------
#lookup function to return text
#check to see if child.tag is actual <key> tag and if text is actual text in variable
def lookup(d, code):
    found = False
    for child in d:
        if found: return child.text
        if child.tag == 'key' and child.text == code :
            found = True
    return None

#parse XML file
stuff = ElementTree.parse(fname)
#go through entries in third dictionary
all = stuff.findall('dict/dict/dict')
print 'Dict count:', len(all)
#for all entrys in the third dictionary do this process in the for loop
for entry in all:
#if no track id just skip it
    if( lookup(entry, 'Track ID') is None ): continue

    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')
    genre = lookup(entry, 'Genre')
    #skip if value is blank
    if name is None or artist is None or album is None or genre is None :
        continue
    print name, artist, album, count, rating, length, genre
    #populate outside in
    #sql command to populate
    cur.execute('''INSERT OR IGNORE INTO Genre (name)
        VALUES ( ? )''', ( genre, ) )
    #sql command to input id into variable
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
    genre_id = cur.fetchone()[0]
    #sql command to populate
    cur.execute('''INSERT OR IGNORE INTO Artist (name) 
        VALUES ( ? )''', ( artist, ) )
    #sql command to input id generated into a variable for next execution
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]
    #sql command to populate
    cur.execute(''' INSERT OR IGNORE INTO ALBUM (title, artist_id)
        VALUES ( ?, ? )''', (album, artist_id ) )
    #get album_id into variable
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]
    #populate track
    cur.execute(''' INSERT OR REPLACE INTO Track (title, album_id, genre_id, len, rating, count)
        VALUES (?, ?, ?, ?, ?, ?)''', ( name, album_id, genre_id, length, rating, count) ) 

    conn.commit()












#called key