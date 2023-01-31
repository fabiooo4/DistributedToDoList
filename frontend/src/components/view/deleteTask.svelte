<script>
  import { deleteTask } from "../controller/fetchTasks";

  export let task;
</script>

<button class="btn btn-error btn-xs btn-circle absolute left-0 self-center" on:click={()=>{deleteTask(task.id)}}>
  <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" /></svg>
</button>