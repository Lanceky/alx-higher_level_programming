#!/usr/bin/node

exports.esrever = function (list) {
  let reversed = []; // Initialize an empty array to store reversed elements

  // Loop through the original list from end to start
  for (let i = list.length - 1; i >= 0; i--) {
    reversed.push(list[i]); // Push each element to the reversed array
  }

  return reversed; // Return the reversed array
};

