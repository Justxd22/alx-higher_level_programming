#!/usr/bin/node

const request = require('request');
const link = process.argv[2];

request(link, (error, response, body) => {
    if (error) {
        console.error(error);
        return;
    }
    let users = {};
    const json = JSON.parse(body);
    json.array.forEach(task => {
        if (task.completed !== true) return;
        if (users[task.userId] === undefined) {
            users[task.userId] = 1;
          } else {
            users[task.userId]++;
          }
    });
    console.log(users);
});
