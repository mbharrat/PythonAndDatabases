#import statment to use sql
import sqlite3

#create sql database file called myemaildb.sql
conn = sqlite3.connect('myemaildb.sql')
curr = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

