#!/usr/bin/node
const list = require('./100-data.js').list;

const l = list.map((x, i) => x * i);
console.log(list);
console.log(l);
