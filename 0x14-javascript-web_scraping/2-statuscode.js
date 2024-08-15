#!/usr/bin/node

const request = require('request');

// Ensure we have exactly one argument
if (process.argv.length !== 3) {
  console.error('Usage: ./2-statuscode.js <url>');
  process.exit(1);
}

// URL from the command-line argument
const url = process.argv[2];

// Make GET request
request.get(url, (error, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
