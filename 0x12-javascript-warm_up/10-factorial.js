#!/usr/bin/node

function factorial (x) {
  if (!x || (x === 0)) {
    return 1;
  }
  return x * factorial(x - 1);
}

const num = parseInt(process.argv[2]);
console.log(factorial(num));
