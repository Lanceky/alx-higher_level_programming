#!/usr/bin/node

const fs = require('fs');

// Ensure we have exactly two arguments
if (process.argv.length !== 4) {
  console.error('Usage: ./1-writeme.js <file_path> <string_to_write>');
  process.exit(1);
}

// File path and data from command-line arguments
const filePath = process.argv[2];
const data = process.argv[3];

// Write string to file
fs.writeFile(filePath, data, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});
