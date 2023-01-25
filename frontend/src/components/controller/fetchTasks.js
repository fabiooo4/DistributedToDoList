import { toDoList } from "./store";

let url = "http://127.0.0.1:5000/tasks";

//? Refresh tasks
export const refreshTasks = async () => {
  const tasks = await getTasks();
  toDoList.set(tasks.data);
}

//? Get all tasks from the server
export const getTasks = async () => {
  const response = await fetch(url, { method: "GET" });
  const data = await response.json();
  return data;
}

//? Get a single task from the server
export const getSingle = async (index) => {
  const response = await fetch(url + "/" + index, { method: "GET" });
  const data = await response.json();
  return data;
}

//? Toggle state of a task given its index
export const toggleState = async (index) => {
  const response = await fetch(url + "/" + index, {
    method: "PATCH",
  });
  const data = await response.json();

  return data;
}

//? Delete a task given its index
export const deleteTask = async (index) => {
  const response = await fetch(url + "/" + index, {
    method: "DELETE",
  });
  const data = await response.json();

  refreshTasks();
  return data;
}

//? Add a task to the server
export const addTask = async (task) => {
  const response = await fetch(url, {
    method: 'POST',
    headers: {
      'Content-type': 'application/json'
    },
    body: JSON.stringify(task)
  });

  const data = await response.json();
  refreshTasks();
  return data;
}

//? Edit a task on the server
export const editTask = async (task) => {
  const response = await fetch(url + "/" + task.id, {
    method: "PUT",
    headers: {
      'Content-type': 'application/json'
    },
    body: JSON.stringify(task)
  });
  const data = await response.json();
  refreshTasks();
  return data;
}