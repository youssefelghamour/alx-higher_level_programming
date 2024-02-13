#!/usr/bin/node
const Square = require('./5-square.js');

class Square extends Square {
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
