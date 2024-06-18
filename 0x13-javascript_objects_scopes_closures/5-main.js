#!/usr/bin/node

const Square = require('./5-square');

const s1 = new Square(4);

console.log('Initial Square:');
s1.print();

console.log('\nSquare after doubling:');
s1.double();
s1.print();

