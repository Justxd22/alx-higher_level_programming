#!/usr/bin/node
if (isNaN(parseInt(process.argv.slice(2)))) {
  console.log('Missing size');
} else {
  const x = parseInt(process.argv.slice(2));
  for (let i = 0; i < parseInt(x); i++) {
    console.log('X'.repeat(x));
  }
}
