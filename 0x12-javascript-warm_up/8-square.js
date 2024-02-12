#!/usr/bin/node

const size = parseInt(process.argv[2]);
if (!size) {
  console.log('Missing size');
} else {
  for (let x = 0; x < size; x++) {
    let line = '';
    for (let y = 0; y < size; y++) {
      line += 'X';
    }
    console.log(line);
  }
}
