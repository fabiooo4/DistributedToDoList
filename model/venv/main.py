from urllib import request
from flask import Flask
from flask_cors import CORS
import sqlite3

# run the app: python -m flask --app main.py run
app = Flask(__name__)
CORS(app)

taskdb = "taskdb.db"

def connect(database):
    con = sqlite3.connect(database)
    cur = con.cursor()
    
    database = {
      "db": con,
      "cursor": cur
    }
    
    return database

@app.route('/')
def index():
    out = [{"msg": "index"}]
    return out

#! Tasks list
@app.route('/tasks', methods=["GET"])
def taskList():
    database = connect(taskdb)

    database.get("cursor").execute("""
    SELECT * FROM tasks
    """)
    
    out = []
    for row in database.get("cursor").fetchall():
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
    database = connect(taskdb)
    
    database.get("cursor").execute(f"""
    SELECT * FROM tasks
      WHERE id = ?
    """, (id,))
      
    out = []
    for row in database.get("cursor").fetchall():
      out.append({
        "id": row[0],
        "date": row[1],
        "title": row[2],
        "content": row[3],
        "state": row[4]
      })
    
    return {
      "data": out,
      "exists": len(out) > 0
    }
  
#! Update task
@app.route('/tasks/<int:id>', methods=["PUT"])
def editTask(id):
    database = connect(taskdb)
    
    database.get("cursor").execute(f"""
    UPDATE tasks
      SET date = ?, title = ?, content = ?, state = ?
      WHERE id = ?
    """, (request.json["date"], request.json["title"], request.json["content"], request.json["state"], id))
    database.get("db").commit()
    
    return {
      "updated": True,
    }

#! Delete task
@app.route('/tasks/<int:id>' , methods=["DELETE"])
def taskDelete(id):
    database = connect(taskdb)
    
    database.get("cursor").execute(f"""
    DELETE FROM tasks
      WHERE id = {id} 
    """)
    database.get("db").commit()
    
    return {
      "deleted": True,
    }

#! Create task given a json
@app.route('/tasks', methods=["POST"])
def addTask():  
    database = connect(taskdb)
    
    database.get("cursor").execute("""
    INSERT INTO tasks(id, date, title, content, state) VALUES(?, ?, ?, ?, ?)
    """, (request.json["id"], request.json["date"], request.json["title"], request.json["content"], request.json["state"]))
    database.get("db").commit()
    
    return {
      "created": True,
    }

print("Server started")