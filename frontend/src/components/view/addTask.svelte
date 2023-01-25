<script>
  import { toDoList } from "../controller/store.js";
  import { addTask } from "../controller/fetchTasks";
</script>

<div class="flex justify-center m-4">
  <!--! Button to open modal -->
  <label for="addTaskModal" class="btn btn-secondary">Add new task</label>

  <input type="checkbox" id="addTaskModal" class="modal-toggle" />
  <div class="modal modal-bottom sm:modal-middle">
    <div class="modal-box">
      <h3 class="font-extrabold text-center text-5xl mb-8">Add a new task</h3>
      <div class="modal-body">
        <!--! Title input-->
        <div class="form-control mt-2">
          <label for="title" class="label">
            <span class="label-text font-bold text-lg">Title</span>
          </label>
          <input type="text" name="title" placeholder="Title" class="input input-bordered rounded-lg text-lg" />
        </div>

        <!--! Content input -->
        <div class="form-control mt-2">
          <label for="content" class="label">
            <span class="label-text font-bold text-lg">Description</span>
          </label>
          <textarea placeholder="Description" name="content" class="textarea h-24 textarea-bordered rounded-lg text-lg"></textarea>
        </div>
      </div>

      <div class="modal-action">
        <label for="addTaskModal" class="btn btn-ghost">Cancel</label>
        <label for="addTaskModal" class="btn btn-primary">Add</label>
      </div>
    </div>
  </div>
</div>

