#!/usr/bin/node
const fs = require('fs');
const arg = process.argv[2];

function readMyFILE () {
  fs.readFile(arg, 'utf8', (error, data) => {
    if (error) {
      console.log(error);
      return;
    }
    console.log(data);
  });
}

readMyFILE(arg);
