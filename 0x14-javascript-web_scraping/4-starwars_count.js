#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

const characterUrl = 'https://swapi-api.alx-tools.com/api/people/18/';

request(apiUrl, function (error, response, body) {
  if (!error) {
    const filmsData = JSON.parse(body).results;
    let count = 0;

    for (const film of filmsData) {
      for (const character of film.characters) {
        if (character === characterUrl) {
          count++;
          break;
        }
      }
    }
    console.log(count);
  }
});
