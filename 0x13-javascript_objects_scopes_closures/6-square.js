#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let char = 'X';
    if (c) {
      char = c;
    }
    for (let x = 0; x < this.height; x++) {
      let line = '';
      for (let y = 0; y < this.width; y++) {
        line += char;
      }
      console.log(line);
    }
  }
}

module.exports = Square;
