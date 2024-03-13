#!/usr/bin/node
if (isNaN(parseInt(process.argv.slice(2))) || isNaN(parseInt(process.argv.slice(2)))) {
  console.log('NaN');
} else {
  const x = parseInt(process.argv.slice(2));
  const y = parseInt(process.argv.slice(3));
  console.log(x + y);
}
