#!/usr/bin/node

const request = require('request');
const link = process.argv[2];

request(link, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const json = JSON.parse(body);
  let count = 0;
  json.results.forEach(movie => {
    if (movie.characters.find(character => character.endsWith('/18/'))) {
      count++;
    }
  });
  console.log(count);
});
