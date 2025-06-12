# Create a table Products with columns id, name, and price. Insert 3 rows and print all rows
import sqlite3
conn = sqlite3.connect('yego.shop')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Products')
cur.execute('CREATE TABLE Products (id INTEGER, name TEXT, price REAL)')

cur.execute('INSERT INTO Products VALUES(1,"pen",10)')
cur.execute('INSERT INTO Products VALUES(2,"book",35.2)')
cur.execute('INSERT INTO Products VALUES(3,"rubber",3.7)')

cur.execute('SELECT * FROM Products')
for row in cur.fetchall():
    print(row)

conn.commit()
conn.close()