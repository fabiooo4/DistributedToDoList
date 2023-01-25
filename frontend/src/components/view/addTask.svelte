<script>
  import { addTask, refreshTasks } from "../controller/fetchTasks";

  let title = "";
  let date = "";
  let content = "";
  let modal = "";

  const handleAdd = () => {
    if (title && date && content) {
      let body = {
        "date": date,
        "title": title,
        "content": content
      };

      addTask(body);

      title = "";
      date = "";
      content = "";
      modal = "addTaskModal"; // Prevents the modal from closing
    } else {
      alert("Please fill all the fields");
    }

    refreshTasks();
  };
</script>

<div class="flex justify-center m-4">
  <!--! Button to open modal -->
  <label for="addTaskModal" class="btn btn-secondary">Add new task</label>

  <input type="checkbox" id="addTaskModal" class="modal-toggle" />
  <div class="modal modal-bottom sm:modal-middle">
    <div class="modal-box">
      <h3 class="font-extrabold text-center text-5xl mb-8">Add a new task</h3>
      <div class="modal-body">
        
        <div class="flex flex-row p-0 m-0">
          <!--! Title input -->
          <div class="form-control mr-2">
            <label for="title" class="label">
              <span class="label-text font-bold text-lg">Title</span>
            </label>
            <input type="text" name="title" placeholder="Title" class="input input-bordered rounded-lg text-lg" bind:value={title} />
          </div>
  
          <!--! Date input -->
          <div class="form-control w-full ml-2">
            <label for="title" class="label">
              <span class="label-text font-bold text-lg">Date</span>
            </label>
            <input type="date" name="title" placeholder="Title" class="input input-bordered rounded-lg text-lg" bind:value={date} />
          </div>
        </div>
        
        <!--! Content input -->
        <div class="form-control mt-2">
          <label for="content" class="label">
            <span class="label-text font-bold text-lg">Description</span>
          </label>
          <textarea placeholder="Description" name="content" class="textarea h-24 textarea-bordered rounded-lg text-lg" bind:value={content}></textarea>
        </div>
      </div>

      <div class="modal-action">
        <label for="addTaskModal" class="btn btn-ghost">Cancel</label>
        <label for={modal} class="btn btn-primary" on:click={handleAdd} on:keydown={handleAdd} on:keypress={handleAdd}>Add</label>
      </div>
    </div>
  </div>
</div>

