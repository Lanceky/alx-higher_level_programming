#!/usr/bin/node

const { list } = require('./100-data');

// Compute the new array using map
const newList = list.map((value, index) => value * index);

// Print the original list and the new list
console.log(list);
console.log(newList);

