#!/usr/bin/node

const fs = require('fs');
const request = require('request');

// Ensure we have exactly two arguments
if (process.argv.length !== 4) {
  console.error('Usage: ./5-request_store.js <url> <file_path>');
  process.exit(1);
}

// URL and file path from command-line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Make GET request and write to file
request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    fs.writeFile(filePath, body, 'utf-8', (err) => {
      if (err) {
        console.error(err);
      }
    });
  }
});
