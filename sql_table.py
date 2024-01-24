import sqlite3

conn = sqlite3.connect("site.db")
conn.execute("CREATE TABLE IF NOT EXISTS users(id integer PRIMARY KEY,\
username text,password password)")
conn.commit()

