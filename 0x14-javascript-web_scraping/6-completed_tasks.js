#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const todos = JSON.parse(body);
  const completedTodos = todos.filter(todo => todo.completed);
  const tasksCompleted = {};

  completedTodos.forEach((todo) => {
    if (!tasksCompleted[todo.userId]) {
      tasksCompleted[todo.userId] = 1;
    } else {
      tasksCompleted[todo.userId] += 1;
    }
  });
  console.log(tasksCompleted);
});
