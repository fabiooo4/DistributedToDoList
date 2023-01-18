import sqlite3

con = sqlite3.connect("venv/taskdb.db")
cur = con.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS tasks(id INTEGER PRIMARY KEY, date DATE, title TEXT, content TEXT , state BOOLEAN)
""")
con.commit()

cur = con.cursor()
cur.execute("""
INSERT INTO tasks(id, date, title, content, state) VALUES('0','18/01/2023', 'primo task', 'che bello fare le todolist', False)
""")
cur.execute("""
INSERT INTO tasks(id, date, title, content, state) VALUES('1','19/01/2023', 'secondo task', 'fare i database è il mio hobby preferito', True)
""")
con.commit()