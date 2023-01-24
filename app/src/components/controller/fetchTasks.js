import { onMount } from "svelte";

let url = "http://127.0.0.1:5000/tasks/";
let tasks = null;

onMount(async () => {
  const response = await fetch(url);
  tasks = await response.json();

  console.log(tasks);
});