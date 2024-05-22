#!/usr/bin/node
const request = require('request');
const arg = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${arg}`;

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(JSON.parse(body).title);
});
