#!/usr/bin/node

const arg = process.argv;
let max = parseInt(arg[2]);
let secondMax = -Infinity;

if (!max || (arg.length === 3)) {
  console.log(0);
} else {
  for (let i = 2; i < arg.length; i++) {
    const num = parseInt(arg[i]);
    if (num > max) {
      secondMax = max;
      max = num;
    } else if (num > secondMax && num < max) {
      secondMax = num;
    }
  }
  console.log(secondMax);
}
