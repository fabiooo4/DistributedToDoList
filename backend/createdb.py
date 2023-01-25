import sqlite3

con = sqlite3.connect("taskdb.db")
cur = con.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS tasks(id INTEGER PRIMARY KEY AUTOINCREMENT, date DATE, title TEXT, content TEXT , state BOOLEAN)
""")
con.commit()

cur = con.cursor()
cur.execute("""
INSERT INTO tasks(date, title, content, state) VALUES('18/01/2023', 'Task 1', 'Che bello fare le todolist', False)
""")
cur.execute("""
INSERT INTO tasks(date, title, content, state) VALUES('19/01/2023', 'Task 2', 'Fare i database è il mio hobby preferito', True)
""")

cur.execute("""
INSERT INTO tasks(date, title, content, state) VALUES('20/01/2023', 'Task 3', 'Boh non so che scrivere', False)
""")
con.commit()