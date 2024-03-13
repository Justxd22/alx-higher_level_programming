#!/usr/bin/node
let n = process.argv.slice(2).map(x => Number(x));
console.log(n)
if (n.length >= 1) {
    console.log(n.sort().reverse());
} else {
    console.log(0);
}