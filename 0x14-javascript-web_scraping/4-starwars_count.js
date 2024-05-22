#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const id = 18;
const personUrl = `https://swapi-api.alx-tools.com/api/people/${id}/`;

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const films = JSON.parse(body).results;

  let count = 0;

  films.forEach(film => {
    if (film.characters.some(charurl => charurl === personUrl)) {
      count++;
    }
  });
  console.log(count);
});
