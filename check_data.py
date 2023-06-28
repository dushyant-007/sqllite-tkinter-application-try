import sqlite3

# Create the database connection
conn = sqlite3.connect("class_database.db")

# Create the table
cur = conn.cursor()
cur.execute("select * from students")

a = cur.fetchall()

print(a)
