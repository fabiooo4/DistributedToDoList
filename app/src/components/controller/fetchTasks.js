// Get a single task from the server
export const getTask = async (url, index) => {
  const response = await fetch(url + index.toString(), { method: "GET" });
  const data = await response.json();
  return data;
}