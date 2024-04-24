#!/usr/bin/node

const request = require('request');
const id = process.argv[2];

request(`https://swapi-api.alx-tools.com/api/films/${id}`, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const json = JSON.parse(body);
  console.log(json.title);
});
