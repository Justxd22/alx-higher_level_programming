#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const link = process.argv[2];
const file = process.argv[3];

request(link, (error, response, body) => {
    if (error) {
        console.error(error);
        return;
    }

    fs.writeFile(file, body, (err) => {
        if (err) {
            console.error(err);
            return;
        }
    });
});
