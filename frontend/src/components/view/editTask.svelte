<script>
  import { editTask } from "../controller/fetchTasks";

  export let task;

  let title = task.title;
  let date = task.date;
  let content = task.content;
  $: modal = task.id;

  const clear = () => {
    title = task.title;
    date = task.date;
    content = task.content;
  };

  const close = () => {
    if (modal === "") {
      modal = task.id;
    }
  }
  
  const handleEdit = () => {
    if (title && date) {
      let body = {
        "id": task.id,
        "date": date,
        "title": title,
        "content": content
      };

      editTask(body);

      modal = task.id;
    } else {
      modal = "";
      alert("Please fill all the fields");
    }
  };

</script>

<div class="flex justify-center">
  <!--! Button to open modal -->
  <!-- svelte-ignore a11y-click-events-have-key-events -->
  <label for={modal} class="btn btn-primary btn-sm" on:click={clear}>Edit</label>

  <input type="checkbox" id={modal} class="modal-toggle" />
  <div class="modal modal-bottom sm:modal-middle">
    <div class="modal-box">
      <h3 class="font-extrabold text-center text-5xl mb-8">Edit task</h3>
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
        <!-- svelte-ignore a11y-click-events-have-key-events -->
        <label for={modal} class="btn btn-ghost" on:click={close}>Cancel</label>
        <!-- svelte-ignore a11y-click-events-have-key-events -->
        <label for={modal} class="btn btn-primary" on:click={handleEdit}>Edit</label>
      </div>
    </div>
  </div>
</div>

