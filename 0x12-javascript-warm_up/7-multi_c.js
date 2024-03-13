#!/usr/bin/env node
let x = process.argv.slice(2);
if (isNaN(parseInt(process.argv.slice(2)))) {
    console.log('Missing number of occurrences');
} 
else {
    for (let i = 0; i < parseInt(x); i++) {
      console.log("C is fun");
    }
}
