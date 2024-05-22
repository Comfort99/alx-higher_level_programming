#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${id}`;

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const characters = JSON.parse(body).characters;

  characters.forEach((characterUrl) => {
    request.get(characterUrl, (err, response, characterBody) => {
      if (err) {
        console.log(err);
        return;
      }
      console.log(JSON.parse(characterBody).name);
    });
  });
});
