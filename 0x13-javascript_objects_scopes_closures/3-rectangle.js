#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w === 0 && h === 0 && !Number.isInteger(w) && !Number.isInteger(h)) {
      this.isEmty = true;
    } else {
      this.width = w;
      this.height = h;
      this.isEmpty = false;
    }
  }

  print () {
    let i = 0;
    while (i < this.height) {
      console.log('X'.repeat(this.width));
      i++;
    }
  }
};
