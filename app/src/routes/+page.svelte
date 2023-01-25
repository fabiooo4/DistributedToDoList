<script>
  import Task from '../components/view/task.svelte';
  import AddTask from '../components/view/addTask.svelte';
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

<h1 class="text-6xl text-center font-extrabold m-4">ToDo List</h1>

<AddTask />

<div class='flex flex-col flex-center items-center'>
  {#if $toDoList.length > 0}
    {#each $toDoList as task}
      <Task {task}/>
    {/each}
  {:else}
    <h2 class='text-2xl text-center font-extrabold m-4'>Loading...</h2>
    <!--! Loading spinner -->
    <div class="flex flex-col items-center justify-center col-span-3">
      <div class="flex flex-row items-center justify-center">
        <div class="w-12 h-12 border-dotted border-1 border-t-4 border-zinc-900 rounded-full animate-spin"></div>
      </div>
    </div>
  {/if}
</div>