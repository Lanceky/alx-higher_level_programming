#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  // Initialize a counter variable to store the number of occurrences
  let count = 0;

  // Loop through each element in the list
  for (let i = 0; i < list.length; i++) {
    // Check if the current element is equal to the searchElement
    if (list[i] === searchElement) {
      count++; // Increment the counter if they are equal
    }
  }

  return count; // Return the total count of occurrences
};

