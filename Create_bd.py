import sqlite3 
  
conn = sqlite3.connect('bd_tic-tac-toe.db') 
c = conn.cursor() 
 
c.execute(''' 
    CREATE TABLE users 
    (id INTEGER PRIMARY KEY, 
    username TEXT, 
    wins INTEGER, 
    fails INTEGER) 
''') 

conn.close()
