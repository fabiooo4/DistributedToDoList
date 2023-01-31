<script>
  import { deleteTask } from "../controller/fetchTasks";

  export let task;

  let modal = "delete" + task.id;

  const handleDelete = () => {
    deleteTask(task.id);
  };
</script>

<div class="flex justify-center">
  <!--! Button to open modal -->
  <!-- svelte-ignore a11y-click-events-have-key-events -->
  <label for={modal} class="btn btn-error btn-xs btn-circle absolute left-0 self-center">
    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" /></svg>
  </label>

  <input type="checkbox" id={modal} class="modal-toggle" />
  <div class="modal modal-bottom sm:modal-middle">
    <div class="modal-box">
      <h3 class="font-extrabold text-center text-4xl mb-8">Delete Task</h3>
      <div class="modal-body">
        <h3 class="font-semibold text-center text-xl mb-8">Are you sure you want to delete this task?</h3>

        <div class="modal-action">
          <!-- svelte-ignore a11y-click-events-have-key-events -->
          <label for={modal} class="btn btn-ghost">Cancel</label>
          <!-- svelte-ignore a11y-click-events-have-key-events -->
          <label for={modal} class="btn btn-error" on:click={handleDelete}>Delete</label>
        </div>
      </div>
    </div>
  </div>
</div>