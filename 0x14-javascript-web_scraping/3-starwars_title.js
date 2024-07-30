#!/usr/bin/node

const request = require('request');

// Ensure we have exactly one argument
if (process.argv.length !== 3) {
  console.error('Usage: ./3-starwars_title.js <movie_id>');
  process.exit(1);
}

// Movie ID from the command-line argument
const movieId = process.argv[2];

// API endpoint for Star Wars movie
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Make GET request
request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movie = JSON.parse(body);
    console.log(movie.title);
  }
});
