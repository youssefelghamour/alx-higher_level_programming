#!/usr/bin/node

const arg = process.argv;
let max = parseInt(arg[2]);
if (!max || (arg.length === 3)) {
  console.log(0);
} else {
  for (let i = 2; i < arg.length; i++) {
    const num = parseInt(arg[i]);
    if (num > max) {
      max = num;
    }
  }
  console.log(max);
}
