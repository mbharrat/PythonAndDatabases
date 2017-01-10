#import statment to use sql
import sqlite3

#create sql database file called myemaildb.sql
conn = sqlite3.connect('myemaildb.sqlite')
cur = conn.cursor()

#if table exists, drop table
cur.execute('''
DROP TABLE IF EXISTS Counts''')

#if create table Counts
cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

#usual prompt user for input and open file
fname = raw_input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'mbox-short.txt'
fh = open(fname)
#for loop to get parts we need from whole file
for line in fh:
	#splits lines into just email address
    if not line.startswith('From: ') : continue
    pieces = line.split()
    email = pieces[1]
    ###########################################
    #this is to find domain name and it works
    pieces2 = line.split('@') #split at '@' sign
    org = pieces2[1]
    org = org.rstrip() #elimn. new line char and whitespace from right
    print org
    ###########################################
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org, ))
    #? in email = is placeholder to be filled in w/ whatever you need
    #first thing in tuple is whats in question mark
    #this is done to prevent sql injection
    row = cur.fetchone() #instruction to get row that matches
    if row is None:#if row does not exist then insert
        cur.execute('''INSERT INTO Counts (org, count) 
                VALUES ( ?, 1 )''', ( org, ) )
    else : #if it does then update the count
        cur.execute('UPDATE Counts SET count=count+1 WHERE org = ?', 
            (org, ))
    # This statement commits outstanding changes to disk each 
    # time through the loop - the program can be made faster 
    # by moving the commit so it runs only after the loop completes

	conn.commit() ####need to move this to outside loop?

# https://www.sqlite.org/lang_select.html
#basically prints to screen when table is created and set up
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

print
print "Counts:"
for row in cur.execute(sqlstr) :
    print str(row[0]), row[1]

cur.close()

