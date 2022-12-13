#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) throw error;
  const UserCompleted = {};
  const Tasks = JSON.parse(body);
  const completed = Tasks.filter(Task => Task.completed === true);
  for (const task of completed) {
    if (task.completed && UserCompleted[task.userId] === undefined) {
      UserCompleted[`${task.userId}`] = 0;
    }
    UserCompleted[`${task.userId}`]++;
  }
  console.log(UserCompleted);
});
