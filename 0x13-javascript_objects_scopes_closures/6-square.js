#!/usr/bin/node
const Square = require('./5-square');

module.exports = class Square1 extends Square {
  charPrint (c) {
    if (!c) {
      this.print();
    } else {
      let i = 0;
      while (i < this.height) {
        console.log(c.repeat(this.width));
        i++;
      }
    }
  }
};
