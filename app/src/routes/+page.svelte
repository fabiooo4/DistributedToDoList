<script>
  import Task from '../components/view/task.svelte';
  import { toDoList } from '../components/controller/store.js';
  import { onMount } from 'svelte';

  let url = "http://127.0.0.1:5000/tasks/";
  let tasks = null;

  onMount(async () => {
    const response = await fetch(url, {method:'GET'});
    tasks = await response.json();

    console.log(tasks);
  });

</script>

<h1 class="text-6xl text-center font-extrabold m-4">ToDo List</h1>

<div class='flex flex-col flex-center items-center'>
  {#if $toDoList.length > 0}
    {#each $toDoList as task}
      <Task {task} />
    {/each}
  {:else}
    <h2 class='text-2xl text-center font-extrabold m-4'>No tasks yet</h2>
  {/if}
</div>