#!/usr/bin/node
const n = isNaN(Number(process.argv[2])) ? 1 : Number(process.argv[2]);
function factor (x) {
  if (x === 0) return 1;
  return x * factor(x - 1);
}
console.log(factor(n));
