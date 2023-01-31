<script>
  import { addTask } from "../controller/fetchTasks";

  let title = "";
  let date = "";
  let content = "";
  let noClose = "";

  const clear = () => {
    title = "";
    date = "";
    content = "";
  };

  const handleAdd = () => {
    if (title && date) {
      const body = {
        "date": date,
        "title": title,
        "content": content
      };

      addTask(body);

      noClose = "addTaskModal"; // Prevents the modal from closing
    } else {
      noClose = "";
      alert("Please fill all the fields");
    }

  };
</script>

<div class="flex justify-center m-2">
  <!--! Button to open modal -->
  <!-- svelte-ignore a11y-click-events-have-key-events -->
  <label for="addTaskModal" class="btn btn-secondary p-3 rounded-full" on:click={clear}>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@48,400,0,0" />
    <span class="material-symbols-outlined">
      add
    </span>
  </label>

  <input type="checkbox" id="addTaskModal" class="modal-toggle" />
  <div class="modal modal-bottom sm:modal-middle">
    <div class="modal-box">
      <h3 class="font-extrabold text-center text-5xl mb-8">Add task</h3>
      <div class="modal-body">
        
        <div class="flex flex-col sm:flex-row p-0 m-0">
          <!--! Title input -->
          <div class="form-control w-full sm:w-1/2 m-0 sm:m-2">
            <label for="title" class="label">
              <span class="label-text font-bold text-lg">Title</span>
            </label>
            <input type="text" name="title" placeholder="Title" class="input input-bordered rounded-lg text-lg" bind:value={title} />
          </div>
  
          <!--! Date input -->
          <div class="form-control w-full sm:w-1/2 m-0 sm:m-2">
            <label for="title" class="label">
              <span class="label-text font-bold text-lg">Date</span>
            </label>
            <input type="date" name="title" placeholder="Title" class="input input-bordered rounded-lg text-lg" bind:value={date} />
          </div>
        </div>
        
        <!--! Content input -->
        <div class="form-control mt-2 mx-0 sm:mx-2">
          <label for="content" class="label">
            <span class="label-text font-bold text-lg">Description</span>
          </label>
          <textarea placeholder="Description" name="content" class="textarea h-24 textarea-bordered rounded-lg text-lg" bind:value={content}></textarea>
        </div>
      </div>

      <div class="modal-action">
        <label for="addTaskModal" class="btn btn-ghost">Cancel</label>
        <label for={noClose} class="btn btn-primary" on:click={handleAdd} on:keydown={handleAdd} on:keypress={handleAdd}>Add</label>
      </div>
    </div>
  </div>
</div>

