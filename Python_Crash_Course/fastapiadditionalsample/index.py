from fastapi import FastAPI, HTTPException
from apitodo import todo
from typing import  List
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)
todos: List[todo.Todo] = []

@app.get("/todos")
def getTodos():
    return todos

@app.post("/todo")
def addTodo(todo: todo.Todo):
    global todos
    id = len(todos) + 1
    todo.id = id
    todos.append(todo)
    return {"message": "todo added successfully"}    

@app.delete("/todo/{id}")
def deleteTodo(id: int):
    global todos
    todos = [t for t in todos if t.id != id]
    return {"message": f"Todo with ID {id} deleted successfully"}
    
@app.put("/todo/{id}")
def updateTodo(id: int, todo: todo.Todo):
    global todos
    for index, existing_todo in enumerate(todos):
        if existing_todo.id == id:
            todo.id = id
            todos[index] = todo
            return {"message": f"Todo with ID {id} updated successfully"}
    raise HTTPException(status_code=404, detail=f"Todo with ID {id} not found")
