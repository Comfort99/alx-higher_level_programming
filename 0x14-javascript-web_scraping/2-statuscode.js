#!/usr/bin/node
const request = require('request');
const arg = process.argv[2];

request.get(arg, (err, response) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log('code:', response.statusCode);
});
