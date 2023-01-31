<script>
  import { toggleState } from "../controller/fetchTasks";
  import DeleteTask from "./deleteTask.svelte";
  import EditTask from "./editTask.svelte";

  export let task;
</script>

<div class="card card-compact w-80 m-4 shrink bg-base-100 shadow-xl">
  <div class="card-body">

    <div class="relative z-0">
      <!--! Checkbox -->
      <div class="absolute right-0 z-10">
        <input type="checkbox" checked={task.state} on:click={()=>{toggleState(task.id)}} class="checkbox checkbox-success"/>
      </div>

      <!--! Task title and description -->
      <h2 class="card-title font-bold break-word pr-8">{task.title}</h2>
      <p class="font-medium break-word">{task.content}</p>
    </div>

    <div class="card-actions justify-end mt-2 relative">
      <!--! Date -->
      <p class="text-sm text-base-content-100 relative text-end self-center mr-2">Due to: {task.date}</p>

      <!--! Edit button -->
      <EditTask {task} />

      <!--! Delete button -->
      <DeleteTask {task} />
    </div>
  </div>
</div>
