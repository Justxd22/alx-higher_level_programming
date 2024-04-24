#!/usr/bin/node
const fs = require('fs');

const args = process.argv;
const filePath = args[2];
const data = args[3];

fs.writeFile(filePath, data, (err) => {
  if (err) {
    console.error(err);
  }
});
