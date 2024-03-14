#!/usr/bin/node
const dict = require('./101-data.js').dict;
const D = {};
for (const key in dict) {
  if (D[dict[key]] === undefined) {
    D[dict[key]] = [key];
  } else {
    D[dict[key]].push(key);
  }
}
console.log(D);
