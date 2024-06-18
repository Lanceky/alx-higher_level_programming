#!/usr/bin/node

class Rectangle {
  constructor(w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      // If w or h is not a positive integer or equal to 0, create an empty object
      this.width = undefined;
      this.height = undefined;
    }
  }

  print() {
    if (this.width !== undefined && this.height !== undefined) {
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    }
  }

  rotate() {
    if (this.width !== undefined && this.height !== undefined) {
      // Swap width and height
      [this.width, this.height] = [this.height, this.width];
    }
  }

  double() {
    if (this.width !== undefined && this.height !== undefined) {
      this.width *= 2;
      this.height *= 2;
    }
  }
}

module.exports = Rectangle;

