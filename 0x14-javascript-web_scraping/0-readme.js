#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv[2];

fs.readFile(filePath, 'utf-8', function (err, content) {
  if (content === undefined) {
    console.error(err);
  } else {
    console.log(content);
  }
});
