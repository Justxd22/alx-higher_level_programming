#!/usr/bin/node
const n = process.argv.slice(2).map(x => Number(x));
if (n.length >= 1) {
  console.log(n.sort().reverse()[1]);
} else {
  console.log(0);
}
