#!/usr/bin/node

const request = require('request');

const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;

request(url, function (error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    let count = 0;

    function printCharacter (charUrl) {
      request(charUrl, function (error, response, body) {
        if (!error) {
          console.log(JSON.parse(body).name);
          count++;

          if (count === characters.length) {
            // All characters have been printed
            process.exit(0);
          }
        }
      });
    }

    // Prints characters in order, waits for each request to finish and print before printing the next one
    for (const charUrl of characters) {
      printCharacter(charUrl);
    }
  }
});
