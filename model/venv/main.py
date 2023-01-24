from urllib import request
from flask import Flask
from flask_cors import CORS
import sqlite3

# run the app: python -m flask --app main.py run
app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    out = [{"msg": "index"}]
    return out

#! Tasks list
@app.route('/tasks', methods=["GET"])
def taskList():
    con = sqlite3.connect("taskdb.db")
    cur = con.cursor()

    cur.execute("""
    SELECT * FROM tasks
    """)
    
    out = []
    for row in cur.fetchall():
      out.append({
        "id": row[0],
        "date": row[1],
        "title": row[2],
        "content": row[3],
        "state": row[4]
      })
    
    return {
      "data": out,
      "size": len(out)
    }

#! Single task
@app.route('/tasks/<int:id>')
def taskDetails(id):
    con = sqlite3.connect("taskdb.db")
    cur = con.cursor()
    
    cur.execute(f"""
    SELECT * FROM tasks
      WHERE id = ?
    """, (id,))
      
    out = cur.fetchone()
    out.append({
      "id": out[0],
      "date": out[1],
      "title": out[2],
      "content": out[3],
      "state": out[4]
    })
    
    return {
      "data": out,
    }

#! Delete task
@app.route('/tasks/<int:id>' , methods=["DELETE"])
def taskDelete(id):
    con = sqlite3.connect("taskdb.db")
    cur = con.cursor()
    
    cur.execute(f"""
    DELETE FROM tasks
      WHERE id = {id} 
    """)
    con.commit()
    
    return {
      "deleted": True,
    }

#! Create task
@app.route('/tasks', methods=["POST"])
def taskCreate(body):
  con = sqlite3.connect("taskdb.db")
  cur = con.cursor()
  
  cur.execute(f"""
  INSERT INTO tasks(id, date, title, content, state) VALUES('{body["id"]}','{body["date"]}', '{body["title"]}', '{body["content"]}', '{body["state"]}')
  """)
  con.commit()
  
  return {
    "created": True,
  }

print("Server started")