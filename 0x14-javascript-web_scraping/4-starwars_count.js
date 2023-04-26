#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
let count = 0;

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const movies = JSON.parse(body).results;
  movies.forEach((movie) => {
    movie.characters.forEach((character) => {
      if (character.includes('18')) {
        count++;
      }
    });
  });
  console.log(count);
});
