#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const movie = JSON.parse(body).characters;
  printCharacters(movie, 0);
});

function printCharacters (movie, index) {
  if (index >= movie.length) {
    return;
  }

  request(movie[index], (error, response, body) => {
    if (!error) {
      console.log(JSON.parse(body).name);
      printCharacters(movie, index + 1);
    }
  });
}
