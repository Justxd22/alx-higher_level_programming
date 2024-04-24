#!/usr/bin/node

const request = require('request');
const link = process.argv[2];

request(link, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  console.log(`code: ${response.statusCode}`);
});
