<script>
  import { deleteTask } from "../controller/fetchTasks";

  export let task;
</script>

<div class="card card-compact w-96 m-2 bg-base-100 shadow-xl">
  <div class="card-body">

    <div class="relative z-0">
      <!--! Checkbox -->
      <div class="absolute right-0 z-10">
        <input type="checkbox" checked={task.state} class="checkbox checkbox-success"/>
      </div>

      <!--! Task title and description -->
      <h2 class="card-title font-bold">{task.title}</h2>
      <p class="font-medium">{task.content}</p>
    </div>

    <div class="card-actions justify-end mt-2 relative">
      <!--! Edit button -->
      <button class="btn btn-primary btn-sm">Edit</button>

      <!--! Delete button -->
      <button class="btn btn-error btn-xs btn-circle absolute left-0 self-center" on:click|once={()=>{deleteTask(task.id)}}>
        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" /></svg>
      </button>
    </div>
  </div>
</div>
