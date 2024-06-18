#!/usr/bin/node

const Rectangle = require('./1-rectangle');

const r1 = new Rectangle(2, 3);
console.log(r1);
console.log(r1.width);  // Output: 2
console.log(r1.height); // Output: 3

const r2 = new Rectangle(2, -3);
console.log(r2);
console.log(r2.width);  // Output: 2
console.log(r2.height); // Output: 0 (defaulted to 0)

const r3 = new Rectangle(2);
console.log(r3);
console.log(r3.width);  // Output: 2
console.log(r3.height); // Output: 0 (defaulted to 0)

