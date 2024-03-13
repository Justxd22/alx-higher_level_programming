#!/usr/bin/env node
if (isNaN(parseInt(process.argv.slice(2))) || isNaN(parseInt(process.argv.slice(2))) ) {
    console.log('NaN');
} 
else {
    let x = parseInt(process.argv.slice(2));
    let y = parseInt(process.argv.slice(3));
    console.log(x + y);
}
