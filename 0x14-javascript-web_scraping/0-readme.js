#!/usr/bin/node
const fs = require('fs');
const args = process.argv;
const filePath = args[2];

fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
