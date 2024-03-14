#!/usr/bin/node
const fs = require('fs');

function concatFiles(file1, file2, destination) {
    fs.readFile(file1, 'utf8', (err, data1) => {
        if (err) throw err;

        fs.readFile(file2, 'utf8', (err, data2) => {
            if (err) throw err;

            const concatenatedContent = data1 + data2;

            fs.writeFile(destination, concatenatedContent, (err) => {
                if (err) throw err;
                console.log(`Files ${file1} and ${file2} concatenated successfully to ${destination}`);
            });
        });
    });
}

const [, , file1, file2, destination] = process.argv;
concatFiles(file1, file2, destination);
