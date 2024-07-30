#!/usr/bin/node

const request = require('request');

// Ensure we have exactly one argument
if (process.argv.length !== 3) {
  console.error('Usage: ./6-completed_tasks.js <api_url>');
  process.exit(1);
}

// API URL from the command-line argument
const apiUrl = process.argv[2];

// Make GET request
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const todos = JSON.parse(body);
    const completedTasks = {};

    todos.forEach(todo => {
      if (todo.completed) {
        if (!completedTasks[todo.userId]) {
          completedTasks[todo.userId] = 0;
        }
        completedTasks[todo.userId]++;
      }
    });

    console.log(completedTasks);
  }
});
