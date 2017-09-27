#!/usr/bin/node
// Script to compute the number of tasks completed by user id
const request = require('request');
const requestURL = process.argv[2];

request(requestURL, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const usrTasks = {};
    let taskList = JSON.parse(body);
    for (let task = 0; task < taskList.length; task++) {
      let usr = taskList[task].userId;
      if (usr in usrTasks && taskList[task].completed === true) {
        usrTasks[usr] = usrTasks[usr] + 1;
      } else if (!(usr in usrTasks) && taskList[task].completed === true) {
        usrTasks[usr] = 1;
      } else {
        continue;
      }
    }
    console.log(usrTasks);
  }
});
