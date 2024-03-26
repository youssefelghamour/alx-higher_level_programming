#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
const characterUrl = 'https://swapi-api.alx-tools.com/api/people/18/';

let count = 0;

request(apiUrl, function (error, response, body) {
  if (!error) {
    const filmsData = JSON.parse(body).results;

    for (const film of filmsData) {
      for (const character of film.characters) {
        if (character.endsWith('/18/')) {
          count++;
          break;
        }
      }
    }
  }
  console.log(count);
});
