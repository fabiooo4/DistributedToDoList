import { writable } from "svelte/store";

export const toDoList = writable([
  {
    id: 1,
    title: 'Task 1',
    content: 'Long description lorem ipsum sit amet whatever do you want to write here www.google.com a link to google.com and a link to https://www.google.comLong description lorem ipsum sit amet whatever do you want to write here www.google.com a link to google.com and a link to https://www.google.com',
    state: false
  },
  {
    id: 2,
    title: 'Task 2',
    content: 'Description 2',
    state: true
  },
  {
    id: 3,
    title: 'Task 3',
    content: 'Description 3',
    state: false
  }
]);
export const isAdding = writable(false);