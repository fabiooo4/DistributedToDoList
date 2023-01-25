import sqlite3

con = sqlite3.connect("taskdb.db")
cur = con.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS tasks(id INTEGER PRIMARY KEY AUTOINCREMENT, date TEXT, title TEXT, content TEXT , state BOOLEAN)
""")
con.commit()