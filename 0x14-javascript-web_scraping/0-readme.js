#!/usr/bin/node

const args = process.argv;
const file = args[2];
let fs = require('fs');
fs.readFile(file, 'utf8', (err, data) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log(data);
  });
