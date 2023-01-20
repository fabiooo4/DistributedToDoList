from urllib import request
from flask import Flask
import sqlite3

app = Flask(__name__)

# fetch('/tasks/' + 1, {
#   method: 'DELETE',
#   headers: {
#     'Content-Type': 'application/json'
#   },
# })
# .then(res => res.json())
# .then(data => console.log(data))

@app.route('/')
def index():
    out = [{"msg": "index"}]
    return out

#! Tasks list
@app.route('/tasks', methods=["GET"])
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

#! Single task
@app.route('/tasks/<int:id>')
def taskDetails(id):
    con = sqlite3.connect("venv/taskdb.db")
    cur = con.cursor()
    
    cur.execute(f"""
    SELECT * FROM tasks
      WHERE id = ?
    """, (id,))
      
    out = cur.fetchone()
    return {
      "data": out,
      # error handling
    }

#! Delete task
@app.route('/tasks/<int:id>' , methods=["DELETE"])
def taskDelete(id):
    con = sqlite3.connect("venv/taskdb.db")
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
  con = sqlite3.connect("venv/taskdb.db")
  cur = con.cursor()
  
  body = {"id": 2, "date": "20/01/2023", "title": "terzo task", "content": "che bello creare task", "state": False}
  body = request.get_json()
  cur.execute(f"""
  INSERT INTO tasks(id, date, title, content, state) VALUES('{body["id"]}','{body["date"]}', '{body["title"]}', '{body["content"]}', '{body["state"]}')
  """)
  con.commit()
  
  return {
    "created": True,
  }
  
