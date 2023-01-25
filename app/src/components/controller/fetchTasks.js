let url = "http://127.0.0.1:5000/tasks/";

// Get a single task from the server
export const getTask = async (index) => {
  const response = await fetch(url + index, { method: "GET" });
  const data = await response.json();
  return data;
}

// Delete a task given its index
export const deleteTask = async (index) => {
  const response = await fetch(url + index, {
    method: "DELETE",
  });
  const data = await response.json();
  return data;
}

// Add a task to the server
export const addTask = async (task) => {
  const response = await fetch(url, {
    method: "POST",
    mode: 'cors',
    headers: {
      'Access-Control-Allow-Origin':'http://localhost:5000',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(task)
  });
  const data = await response.json();
  return data;
}

// Update a task on the server
export const updateTask = async (task) => {
  const response = await fetch(url + task.id, {
    method: "PUT",
    mode: 'cors',
    headers: {
      'Access-Control-Allow-Origin':'http://localhost:5000',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(task)
  });
  const data = await response.json();
  return data;
}