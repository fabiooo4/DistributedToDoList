import { writable } from "svelte/store";

export const toDoList = writable([
  {
    id: 1,
    title: 'Task 1',
    description: 'Long description lorem ipsum sit amet whatever do you want to write here www.google.com a link to google.com and a link to https://www.google.comLong description lorem ipsum sit amet whatever do you want to write here www.google.com a link to google.com and a link to https://www.google.com',
    completed: false
  },
  {
    id: 2,
    title: 'Task 2',
    description: 'Description 2',
    completed: true
  },
  {
    id: 3,
    title: 'Task 3',
    description: 'Description 3',
    completed: false
  }
]);
export const isAdding = writable(false);