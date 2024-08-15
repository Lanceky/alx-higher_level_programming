#!/usr/bin/node

const request = require('request');

// Ensure we have exactly one argument
if (process.argv.length !== 3) {
  console.error('Usage: ./100-starwars_characters.js <movie_id>');
  process.exit(1);
}

// Movie ID from the command-line argument
const movieId = process.argv[2];

// API endpoint for Star Wars movie
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Make GET request to get film details
request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const film = JSON.parse(body);
    const characterUrls = film.characters;

    // Fetch character details
    characterUrls.forEach((characterUrl) => {
      request.get(characterUrl, (error, response, body) => {
        if (error) {
          console.error(error);
        } else {
          const character = JSON.parse(body);
          console.log(character.name);
        }
      });
    });
  }
});
