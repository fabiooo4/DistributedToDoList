from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    out = [{"msg": "index"}]
    return out


@app.route('/tasks', methods=["GET", "POST"])
def taskList():
    con = sqlite3.connect("venv/taskdb.db")
    cur = con.cursor()

    cur.execute("""
    SELECT * FROM tasks
    """)
    
    out = cur.fetchall()
    return {
      "data": out,
      "size": len(out)
    }


@app.route('/tasks/<int:id>')
def taskDetails(id):
    con = sqlite3.connect("venv/taskdb.db")
    cur = con.cursor()
    
    cur.execute(f"""
    SELECT * FROM tasks
      WHERE id = {id} 
    """)
      
    out = cur.fetchone()
    return {
      "data": out,
      "size": len(out)
    }