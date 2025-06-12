# Using Databases and SQL 
- `Database:` A structured collection of data.
- `Relational Database:` Stores data in tables (rows and columns).
- `SQL (Structured Query Language):` Used to interact with relational databases.

## SQLite in Python
- Python provides a built-in module called sqlite3 for interacting with SQLite databases.
- SQLite is lightweight and stores data in a single file.

## Common SQL Commands
- `SELECT:` Read data
- `INSERT:` Add new rows
- `UPDATE:` Modify existing rows
- `DELETE:` Remove rows
- `CREATE TABLE:` Define new table
- `DROP TABLE:` Delete table

## Basic steps
````
import sqlite3

# Connect to a database (or create it)
conn = sqlite3.connect('mydata.db')
cur = conn.cursor()

# Create a table
cur.execute('CREATE TABLE IF NOT EXISTS Users (id INTEGER, name TEXT)')

# Insert data
cur.execute('INSERT INTO Users (id, name) VALUES (?, ?)', (1, 'Alice'))
cur.execute('INSERT INTO Users (id, name) VALUES (?, ?)', (2, 'Bob'))

# Query data
cur.execute('SELECT * FROM Users')
for row in cur.fetchall():
    print(row)

# Save (commit) the changes
conn.commit()

# Close the connection
conn.close()
````
