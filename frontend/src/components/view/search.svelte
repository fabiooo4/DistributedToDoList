<script>
  import { toDoList } from "../controller/store.js";
  import { refreshTasks } from "../controller/fetchTasks.js";
  export let search = "";

  $: if (search !== "") {
    toDoList.update((tasks) => {
      return tasks.filter((task) => {
        return task.title.toLowerCase().includes(search.toLowerCase());
      });
    });
  } else {
    refreshTasks();
  }
</script>

<input type="text" name="search" placeholder="Search" class="input input-bordered self-center rounded-full text-lg font-semibold w-fill" bind:value={search} />