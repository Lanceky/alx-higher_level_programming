#!/usr/bin/node

const Square = require('./5-square');

class SquareWithCharPrint extends Square {
  constructor(size) {
    super(size);
  }

  charPrint(c) {
    if (c === undefined) {
      c = 'X';
    }
    // Print the square using character c
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = SquareWithCharPrint;

