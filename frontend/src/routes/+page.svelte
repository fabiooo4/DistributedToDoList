<script>
  import Task from '../components/view/task.svelte';
  import AddTask from '../components/view/addTask.svelte';
  import Search from '../components/view/search.svelte';
  import { toDoList } from '../components/controller/store.js';
  import { onMount } from 'svelte';

  let url = "http://127.0.0.1:5000/";

  // Load all tasks from the database
  onMount(async () => {
    const response = await fetch(url + "tasks", { method:'GET' });
    let tasks = await response.json();

    toDoList.set(tasks.data);
  });
</script>

<h1 class="text-8xl text-center font-extrabold m-4">ToDo List</h1>

<div class="flex flex-row justify-center flex-wrap">
  <Search />
  <AddTask />
</div>

<div class='flex flex-row flex-wrap justify-center items-center w-screen pb-10'>
  {#if $toDoList.length > 0}
    {#each $toDoList as task}
      <Task {task}/>
    {/each}
  {:else}
    <h2 class='text-2xl text-center font-bold m-4'>No tasks found...</h2>
  {/if}
</div>