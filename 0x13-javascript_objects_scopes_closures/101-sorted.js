#!/usr/bin/node
const dict = require('./101-data.js').dict;
let D = {};
for (let key in dict) {
  if (D[dict[key]] === undefined) {
    D[dict[key]] = [key];
  } else {
    D[dict[key]].push(key);
  }
}
console.log(D);