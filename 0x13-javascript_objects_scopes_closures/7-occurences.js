#!/usr/bin/node

let count = 0; // Initialize a counter variable outside the function scope

exports.logMe = function (item) {
  console.log(`${count}: ${item}`); // Print the current count and the item
  count++; // Increment the count for the next call
};

