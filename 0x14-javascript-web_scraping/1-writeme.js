#!/usr/bin/node
const fs = require('fs');
const arg2 = process.argv[2];
const arg3 = process.argv[3];

function writeMyFILE () {
  fs.writeFile(arg2, arg3, err => {
    if (err) {
      console.log(err);
    }
  });
}

writeMyFILE(arg2, arg3);
