#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const todos = JSON.parse(body);
  const completed = {};

  todos.forEach((todo) => {
    const userId = todo.userId;

    if (todo.completed) {
      completed[userId] = (completed[userId] || 0) + 1;
    }
  });
  console.log(completed);
});
