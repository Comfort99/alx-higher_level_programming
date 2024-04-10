#!/usr/bin/node
module.exports = class Reactangle {
  constructor (w, h) {
    if (w === 0 && h === 0 && !Number.isInteger(w) && !Number.isInteger(h)) {
      this.isEmpty = true;
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

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
