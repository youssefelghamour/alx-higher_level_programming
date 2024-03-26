#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, function (error, response, body) {
  if (!error) {
    const completedTasks = {};
    const tasks = JSON.parse(body);

    for (const task of tasks) {
      if (task.completed) {
        const userId = task.userId;

        if (completedTasks[userId] === undefined) {
          completedTasks[userId] = 0;
        }

        completedTasks[userId]++;
      }
    }
    console.log(completedTasks);
  }
});
