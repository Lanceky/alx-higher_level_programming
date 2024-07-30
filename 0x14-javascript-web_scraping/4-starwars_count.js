#!/usr/bin/node

const request = require('request');

// Ensure we have exactly one argument
if (process.argv.length !== 3) {
  console.error('Usage: ./4-starwars_count.js <api_url>');
  process.exit(1);
}

// API URL from the command-line argument
const apiUrl = process.argv[2];

// Make GET request to fetch film details
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const films = JSON.parse(body);
  let count = 0;

  // Helper function to process each film
  const processFilm = (film, callback) => {
    const characters = film.characters || [];
    const wedgeAntillesUrl = 'https://swapi-api.alx-tools.com/api/people/18/';

    // Check if Wedge Antilles is in this film
    const isInFilm = characters.some(characterUrl => characterUrl === wedgeAntillesUrl);
    if (isInFilm) {
      count++;
    }
    
    callback();
  };

  // Process each film
  let completedRequests = 0;
  films.results.forEach(film => {
    processFilm(film, () => {
      completedRequests++;
      // After processing all films, print the count
      if (completedRequests === films.results.length) {
        console.log(count);
      }
    });
  });
});
