#!/usr/bin/node

let file = process.argv[2];
let fs = require('fs');
fs.readFile(file, 'utf8', (err, data) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log(data);
  });
